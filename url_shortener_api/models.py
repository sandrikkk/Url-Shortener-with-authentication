# Create your models here.
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, is_premium=False, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, is_premium=is_premium, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, is_premium=True, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, is_premium=is_premium, **extra_fields)

class CustomUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_active = models.BooleanField(default=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_premium = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)


    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
         return self.is_superuser

    USERNAME_FIELD = 'email'
    objects = CustomUserManager()

class Link(models.Model):
    original_link = models.URLField(max_length=250)
    shortened_link = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_premium = models.BooleanField(default=False)
    count = models.IntegerField(default=0)
    custom_url = models.CharField(blank=True, null=True, max_length=250)

    class Meta:
        ordering = ('-created_at',)
    
    def increase_short_id_counter(self):
        self.count += 1
        self.save()

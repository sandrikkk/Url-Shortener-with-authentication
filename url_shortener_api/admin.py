from os import link
from django.contrib import admin
from . models import Link
from . models import CustomUser
# Register your models here.
admin.site.register(Link)
admin.site.register(CustomUser)
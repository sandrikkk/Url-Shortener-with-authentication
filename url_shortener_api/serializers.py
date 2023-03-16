from random import choices
from string import ascii_letters
from url_shortener_api.models import CustomUser
from rest_framework import serializers
from .models import Link
from rest_framework_simplejwt.tokens import RefreshToken

class UserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only = True)
    _id = serializers.SerializerMethodField(read_only = True)
    token = serializers.SerializerMethodField(read_only = True)
    class Meta:
        model = CustomUser
        fields = ['id', '_id','email', 'name', "is_staff", 'is_premium', 'token']


    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)

    def get__id(self,obj):
        return obj.id

    def get_name(self, obj):
        if obj.first_name and obj.last_name:
            name = obj.first_name + " " + obj.last_name
        else:
            name = obj.email
        return name



class LinkSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)
    count = serializers.IntegerField(read_only=True)
    shortened_link = serializers.URLField(read_only=True)
    is_premium = serializers.SerializerMethodField(read_only = True)
    custom_url = serializers.CharField(allow_null=True, max_length=250)
    # user = serializers.SerializerMethodField(read_only = True)


    class Meta:
        model = Link
        fields = ['id', 'original_link', 'shortened_link', 'created_at', 'count', 'is_premium', 'custom_url']

    def get_is_premium(self, obj):
        user = self.context['user']
        if user.is_premium:
            return True
        else:
            return obj.is_premium

    # def get_user(self,obj):
    #     return self.context['user']

    def create(self, validated_data):
        url = super().create(validated_data)
        url.save()  # save in db
        random_string = ''.join(choices(ascii_letters, k=6))

        original_link = validated_data.get('original_link')
        custom_string = validated_data.get('custom_url')
        user = self.context['user']

        if (not custom_string) and (not user.is_premium):
            self.add_error('custom_url', 'You are not a premium user and did not provide a custom URL')

        if (custom_string and user.is_premium):
            random_string = custom_string

        host = self.context.get('request').headers.get('host')

        if original_link:
            link = 'http://' + host + '/api/' + random_string + '/'
            url.shortened_link = link
            url.save()
        return url

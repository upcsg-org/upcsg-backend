from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import LoginSerializer
from django.core.exceptions import ValidationError
from .models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False, allow_blank=True)
    class Meta:
        model = User
        exclude = ["user_permissions", "groups"]
        
class LoginSerializer(LoginSerializer):
    username = serializers.CharField()
    password = serializers.CharField()

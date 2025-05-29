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

class CustomRegisterSerializer(RegisterSerializer):
    """Custom registration serializer that disables password validation."""
    
    def validate_email(self, email):
        if User.objects.filter(email__iexact=email).exists():
            raise serializers.ValidationError("A user with that email already exists.")
        return email
    
    def validate_password1(self, password):
        """Override to remove password validation."""
        return password
    
    def validate_password2(self, password):
        """Override to remove password validation."""
        return password
        
class LoginSerializer(LoginSerializer):
    username = serializers.CharField()
    password = serializers.CharField()

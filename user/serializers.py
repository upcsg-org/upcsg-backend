from rest_framework import serializers
from .models import User
from dj_rest_auth.registration.serializers import RegisterSerializer
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {
            'password': {'write_only': True}
        }

class CustomRegisterSerializer(RegisterSerializer):
    username = None  # Remove username field
    email = serializers.EmailField(required=True)
    
    def validate_email(self, email):
        """
        Validate that the email is unique.
        """
        UserModel = get_user_model()
        if UserModel.objects.filter(email=email).exists():
            raise serializers.ValidationError("A user with this email already exists.")
        return email
    
    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        if 'username' in data:
            del data['username']  # Remove username from cleaned data
        return data
    
    def custom_signup(self, request, user):
        pass  # We don't need to do anything extra on signup

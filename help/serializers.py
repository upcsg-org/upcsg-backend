from rest_framework import serializers
from .models import Concern

class ConcernSerializer(serializers.ModelSerializer):
    class Meta:
        model = Concern
        fields = '__all__'

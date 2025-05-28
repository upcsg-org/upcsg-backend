from rest_framework import serializers
from .models import Term, Officer

class OfficerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Officer
        fields = ['id', 'image_url', 'name', 'position', 'yearlevel', 'created_at', 'updated_at']

class TermSerializer(serializers.ModelSerializer):
    officers = OfficerSerializer(many=True, read_only=True)

    class Meta:
        model = Term
        fields = ['id', 'startYear', 'endYear', 'officers', 'created_at', 'updated_at'] 
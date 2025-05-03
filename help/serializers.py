from rest_framework import serializers
from .models import Concern
from user.models import User
class ConcernSerializer(serializers.ModelSerializer):
    class Meta:
        model = Concern
        fields = '__all__'

class EmailFormSerializer(serializers.Serializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False, allow_null=True)
    name = serializers.CharField(max_length=255)
    email = serializers.EmailField()
    content = serializers.CharField()

from rest_framework import serializers
from .models import Merch, MerchVariant, Bundle

class MerchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Merch
        fields = '__all__'

class MerchVariantSerializer(serializers.ModelSerializer):
    merch = MerchSerializer()

    class Meta:
        model = MerchVariant
        fields = '__all__'

class BundleSerializer(serializers.ModelSerializer):
    merch = MerchSerializer(many=True)

    class Meta:
        model = Bundle
        fields = '__all__'

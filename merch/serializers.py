from rest_framework import serializers
from .models import MerchType, MerchSize, Merch, MerchVariant, Bundle

class MerchSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MerchSize
        fields = ['id', 'name', 'description', 'created_at', 'updated_at']

class MerchTypeSerializer(serializers.ModelSerializer):
    sizes = MerchSizeSerializer(many=True, read_only=True)

    class Meta:
        model = MerchType
        fields = ['id', 'name', 'description', 'sizes', 'created_at', 'updated_at']

MerchSizeSerializer.Meta.fields = ['id', 'name', 'description', 'merch_type', 'merch_type_id', 'created_at', 'updated_at']
MerchSizeSerializer.merch_type = MerchTypeSerializer(read_only=True)
MerchSizeSerializer.merch_type_id = serializers.PrimaryKeyRelatedField(
    queryset=MerchType.objects.all(), source='merch_type', write_only=True
)



class MerchSerializer(serializers.ModelSerializer):
    merch_type = MerchTypeSerializer(read_only=True)
    merch_type_id = serializers.PrimaryKeyRelatedField(
        queryset=MerchType.objects.all(), source='merch_type', write_only=True
    )

    class Meta:
        model = Merch
        fields = ['id', 'name', 'description','image', 'merch_type', 'merch_type_id', 'created_at', 'updated_at']
        



class MerchVariantSerializer(serializers.ModelSerializer):
    merch = MerchSerializer(read_only=True)  # safe now, MerchSerializer already defined
    merch_id = serializers.PrimaryKeyRelatedField(
        queryset=Merch.objects.all(), source='merch', write_only=True
    )

    size = MerchSizeSerializer(read_only=True)
    size_id = serializers.PrimaryKeyRelatedField(
        queryset=MerchSize.objects.all(), source='size', write_only=True
    )

    class Meta:
        model = MerchVariant
        fields = [
            'id', 'name', 'price', 'image', 'variant', 'is_bestseller',
            'is_available', 'is_limited', 'on_sale', 'quantity',
            'merch', 'merch_id', 'size', 'size_id', 'created_at', 'updated_at'
        ]



class BundleSerializer(serializers.ModelSerializer):
    merch = MerchSerializer(read_only=True, many=True)
    merch_ids = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Merch.objects.all(), source='merch', write_only=True
    )

    class Meta:
        model = Bundle
        fields = ['id', 'name','description', 'price','image', 'merch', 'merch_ids', 'created_at', 'updated_at']

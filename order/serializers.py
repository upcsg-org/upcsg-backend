from rest_framework import serializers
from .models import Order, OrderItem
from merch.serializers import MerchVariantSerializer
from user.serializers import UserSerializer
from user.models import User
from merch.models import MerchVariant

class OrderSerializer(serializers.ModelSerializer):
    buyer_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='buyer', write_only=True
    )
    buyer = UserSerializer(read_only=True)
    class Meta:
        model = Order
        fields = '__all__'

class OrderItemSerializer(serializers.ModelSerializer):
    order_id = serializers.PrimaryKeyRelatedField(
        queryset=Order.objects.all(), source='order', write_only=True
    )
    order = OrderSerializer(read_only=True)
    merch_variant_id = serializers.PrimaryKeyRelatedField(
        queryset=MerchVariant.objects.all(), source='merch_variant', write_only=True
    )
    merch_variant = MerchVariantSerializer(read_only=True)

    class Meta:
        model = OrderItem
        fields = '__all__'

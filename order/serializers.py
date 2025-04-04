from rest_framework import serializers
from .models import Order, OrderItem
from merch.serializers import MerchSerializer
from user.serializers import UserSerializer

class OrderSerializer(serializers.ModelSerializer):
    buyer = UserSerializer()

    class Meta:
        model = Order
        fields = '__all__'

class OrderItemSerializer(serializers.ModelSerializer):
    order = OrderSerializer()
    merch = MerchSerializer()

    class Meta:
        model = OrderItem
        fields = '__all__'

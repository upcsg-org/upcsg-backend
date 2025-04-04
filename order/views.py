from main.utils.generic_api import GenericView
from .models import Order, OrderItem
from .serializers import OrderSerializer, OrderItemSerializer
from rest_framework.permissions import IsAuthenticated

class OrderView(GenericView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer 
    permission_classes = [IsAuthenticated]
    cache_key_prefix = "order"

class OrderItemView(GenericView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [IsAuthenticated]
    cache_key_prefix = "order_item"

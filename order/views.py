from main.utils.generic_api import GenericView
from .models import Order, OrderItem
from .serializers import OrderSerializer, OrderItemSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.db.models import Q

class OrderView(GenericView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer 
    permission_classes = [IsAuthenticated]
    allowed_methods = ["list", "create"]
    
    def filter_queryset(self, filters, excludes):
        filter_q = Q(**filters)
        exclude_q = Q(**excludes)
        return self.queryset.filter(filter_q).exclude(exclude_q).filter(buyer=self.request.user)
    
    def pre_create(self, request):
        request.data['buyer_id'] = self.request.user.id

class OrderItemView(GenericView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [IsAuthenticated]
    allowed_methods = ["list", "create"]

class ManageOrderView(GenericView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAdminUser]
    
class ManageOrderItemView(GenericView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [IsAdminUser]

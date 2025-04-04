from django.urls import path
from .views import OrderView, OrderItemView

urlpatterns = [
    path('order/', OrderView.as_view({'get': 'list', 'post': 'create'}), name='order'),
    path('order/<int:pk>/', OrderView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='order_detail'),
    path('order-item/', OrderItemView.as_view({'get': 'list', 'post': 'create'}), name='order_item'),
    path('order-item/<int:pk>/', OrderItemView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='order_item_detail'),
]

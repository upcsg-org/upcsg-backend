from django.urls import path
from .views import OrderView, OrderItemView, ManageOrderView, ManageOrderItemView

urlpatterns = [
    path('', OrderView.as_view({'get': 'list', 'post': 'create'}), name='order'),
    path('<int:pk>/', OrderView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='order_detail'),
    path('order-item/', OrderItemView.as_view({'get': 'list', 'post': 'create'}), name='order_item'),
    path('order-item/<int:pk>/', OrderItemView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='order_item_detail'),
    path('manage/', ManageOrderView.as_view({'get': 'list', 'post': 'create'}), name='manage_order'),
    path('manage/<int:pk>/', ManageOrderView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='manage_order_detail'),
    path('manage/order-item/', ManageOrderItemView.as_view({'get': 'list', 'post': 'create'}), name='manage_order_item'),
    path('manage/order-item/<int:pk>/', ManageOrderItemView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='manage_order_item_detail'),
]

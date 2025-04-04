from django.urls import path
from .views import MerchView, MerchVariantView, BundleView, ManageMerchView, ManageMerchVariantView, ManageBundleView

urlpatterns = [
    path('merch/', MerchView.as_view({'get': 'list'}), name='merch'),
    path('merch/<int:pk>/', MerchView.as_view({'get': 'retrieve'}), name='merch_detail'),
    path('merch/manage/', ManageMerchView.as_view({'post': 'create'}), name='manage_merch'),
    path('merch/manage/<int:pk>/', ManageMerchView.as_view({'put': 'update', 'delete': 'destroy'}), name='manage_merch_detail'),
    path('merch-variant/', MerchVariantView.as_view({'get': 'list'}), name='merch_variant'),
    path('merch-variant/<int:pk>/', MerchVariantView.as_view({'get': 'retrieve'}), name='merch_variant_detail'),
    path('merch-variant/manage/', ManageMerchVariantView.as_view({'post': 'create'}), name='manage_merch_variant'),
    path('merch-variant/manage/<int:pk>/', ManageMerchVariantView.as_view({'put': 'update', 'delete': 'destroy'}), name='manage_merch_variant_detail'),
    path('bundle/', BundleView.as_view({'get': 'list'}), name='bundle'),
    path('bundle/<int:pk>/', BundleView.as_view({'get': 'retrieve'}), name='bundle_detail'),
    path('bundle/manage/', ManageBundleView.as_view({'post': 'create'}), name='manage_bundle'),
    path('bundle/manage/<int:pk>/', ManageBundleView.as_view({'put': 'update', 'delete': 'destroy'}), name='manage_bundle_detail'),
]

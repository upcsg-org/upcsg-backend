from django.urls import path
from .views import MerchView, MerchVariantView, BundleView, ManageMerchView, ManageMerchVariantView, ManageBundleView, MerchTypeView, ManageMerchTypeView, MerchSizeView, ManageMerchSizeView

urlpatterns = [
    path('product/', MerchView.as_view({'get': 'list'}), name='merch'),
    path('product/<int:pk>/', MerchView.as_view({'get': 'retrieve'}), name='merch_detail'),
    path('product/manage/', ManageMerchView.as_view({'post': 'create'}), name='manage_merch'),
    path('product/manage/<int:pk>/', ManageMerchView.as_view({'put': 'update', 'delete': 'destroy'}), name='manage_merch_detail'),
    
    path('merch-variant/', MerchVariantView.as_view({'get': 'list'}), name='merch_variant'),
    path('merch-variant/<int:pk>/', MerchVariantView.as_view({'get': 'retrieve'}), name='merch_variant_detail'),
    path('merch-variant/manage/', ManageMerchVariantView.as_view({'post': 'create'}), name='manage_merch_variant'),
    path('merch-variant/manage/<int:pk>/', ManageMerchVariantView.as_view({'put': 'update', 'delete': 'destroy'}), name='manage_merch_variant_detail'),
    
    path('merch-type/', MerchTypeView.as_view({'get': 'list'}), name='merch_type'),
    path('merch-type/<int:pk>/', MerchTypeView.as_view({'get': 'retrieve'}), name='merch_type_detail'),
    path('merch-type/manage/', ManageMerchTypeView.as_view({'post': 'create'}), name='manage_merch_type'),
    path('merch-type/manage/<int:pk>/', ManageMerchTypeView.as_view({'put': 'update', 'delete': 'destroy'}), name='manage_merch_type_detail'),
    
    path('merch-size/', MerchSizeView.as_view({'get': 'list'}), name='merch_size'),
    path('merch-size/<int:pk>/', MerchSizeView.as_view({'get': 'retrieve'}), name='merch_size_detail'),
    path('merch-size/manage/', ManageMerchSizeView.as_view({'post': 'create'}), name='manage_merch_size'),
    path('merch-size/manage/<int:pk>/', ManageMerchSizeView.as_view({'put': 'update', 'delete': 'destroy'}), name='manage_merch_size_detail'),
    
    path('bundle/', BundleView.as_view({'get': 'list'}), name='bundle'),
    path('bundle/<int:pk>/', BundleView.as_view({'get': 'retrieve'}), name='bundle_detail'),
    path('bundle/manage/', ManageBundleView.as_view({'post': 'create'}), name='manage_bundle'),
    path('bundle/manage/<int:pk>/', ManageBundleView.as_view({'put': 'update', 'delete': 'destroy'}), name='manage_bundle_detail'),
]

from django.urls import path
from .views import (
    TermView, ManageTermView,
    OfficerView, ManageOfficerView
)

urlpatterns = [
    # Term URLs
    path('terms/', TermView.as_view({'get': 'list'}), name='term-list'),
    path('terms/<int:pk>/', TermView.as_view({'get': 'retrieve'}), name='term-detail'),
    path('terms/manage/', ManageTermView.as_view({'post': 'create'}), name='term-manage'),
    path('terms/manage/<int:pk>/', ManageTermView.as_view({'put': 'update', 'delete': 'destroy'}), name='term-manage-detail'),

    # Officer URLs
    path('officers/', OfficerView.as_view({'get': 'list'}), name='officer-list'),
    path('officers/<int:pk>/', OfficerView.as_view({'get': 'retrieve'}), name='officer-detail'),
    path('officers/manage/', ManageOfficerView.as_view({'post': 'create'}), name='officer-manage'),
    path('officers/manage/<int:pk>/', ManageOfficerView.as_view({'put': 'update', 'delete': 'destroy'}), name='officer-manage-detail'),
] 
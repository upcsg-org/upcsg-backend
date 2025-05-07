from django.urls import path
from .views import ManageConcernView, TrackConcernView, EmailFormView

urlpatterns = [
    path('concerns/manage/', ManageConcernView.as_view({'get': 'list'}), name='manage-concern'),
    path('concerns/manage/<int:pk>/', ManageConcernView.as_view({'put': 'update', 'delete': 'destroy'}), name='manage-concern-detail'),
    path('concerns/track/', TrackConcernView.as_view({'get': 'list'}), name='track-concern'),
    path('concerns/track/<int:pk>/', TrackConcernView.as_view({'get': 'retrieve'}), name='track-concern-detail'),
    path('concerns/', EmailFormView.as_view(), name='email-form'),
]

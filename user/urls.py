from django.urls import path, include
from .views import UserView, ManageUserView

urlpatterns = [
    path("", include("dj_rest_auth.urls")),
    path("registration/", include("dj_rest_auth.registration.urls")),
    path("user/", UserView.as_view({'put': 'update'}), name='user'),
    path("manage/", ManageUserView.as_view({'get': 'list', 'post': 'create'}), name='manage_user'),
    path("manage/<int:pk>/", ManageUserView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='manage_user_detail'),
]

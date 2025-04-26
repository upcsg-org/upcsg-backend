from django.urls import path
from .views import ArticleView, ManageArticleView, EventView, ManageEventView, ScholarshipView, ManageScholarshipView, InternshipView, ManageInternshipView, AnnouncementView, ManageAnnouncementView, DashboardView

urlpatterns = [
    path('articles/', ArticleView.as_view({'get': 'list'}), name='article-list'),
    path('articles/<int:pk>/', ArticleView.as_view({'get': 'retrieve'}), name='article-detail'),
    path('articles/manage/', ManageArticleView.as_view({'post': 'create', 'put': 'update', 'delete': 'destroy'}), name='manage-article'),

    path('events/', EventView.as_view({'get': 'list'}), name='event-list'),
    path('events/<int:pk>/', EventView.as_view({'get': 'retrieve'}), name='event-detail'),
    path('events/manage/', ManageEventView.as_view({'post': 'create'}), name='create-event'),
    path('events/manage/<int:pk>/', ManageEventView.as_view({'put': 'update', 'delete': 'destroy'}), name='manage-event'),

    path('scholarships/', ScholarshipView.as_view({'get': 'list'}), name='scholarship-list'),
    path('scholarships/<int:pk>/', ScholarshipView.as_view({'get': 'retrieve'}), name='scholarship-detail'),
    path('scholarships/manage/', ManageScholarshipView.as_view({'post': 'create'}), name='create-scholarship'),
    path('scholarships/manage/<int:pk>/', ManageScholarshipView.as_view({'put': 'update', 'delete': 'destroy'}), name='manage-scholarship'),

    path('internships/', InternshipView.as_view({'get': 'list'}), name='internship-list'),
    path('internships/<int:pk>/', InternshipView.as_view({'get': 'retrieve'}), name='internship-detail'),
    path('internships/manage/', ManageInternshipView.as_view({'post': 'create'}), name='create-internship'),
    path('internships/manage/<int:pk>/', ManageInternshipView.as_view({'put': 'update', 'delete': 'destroy'}), name='manage-internship'),

    path('announcements/', AnnouncementView.as_view({'get': 'list'}), name='announcement-list'),
    path('announcements/<int:pk>/', AnnouncementView.as_view({'get': 'retrieve'}), name='announcement-detail'),
    path('announcements/manage/', ManageAnnouncementView.as_view({'post': 'create'}), name='create-announcement'),
    path('announcements/manage/<int:pk>/', ManageAnnouncementView.as_view({'put': 'update', 'delete': 'destroy'}), name='manage-announcement'),

    path('dashboard/', DashboardView.as_view(), name='dashboard'),
]

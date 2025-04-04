from main.utils.generic_api import GenericView
from .models import Article, Event, Scholarship, Internship, Announcement
from .serializers import ArticleSerializer, EventSerializer, ScholarshipSerializer, InternshipSerializer, AnnouncementSerializer
from rest_framework.permissions import IsAdminUser
class ArticleView(GenericView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    cache_key_prefix = "article"
    allowed_methods = ["list", "retrieve"]
    
class ManageArticleView(GenericView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAdminUser]
    cache_key_prefix = "manage-article"
    allowed_methods = ["create", "update", "destroy"]

class EventView(GenericView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    cache_key_prefix = "event"
    allowed_methods = ["list", "retrieve"]

class ManageEventView(GenericView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAdminUser]
    cache_key_prefix = "manage-event"
    allowed_methods = ["create", "update", "destroy"]

class ScholarshipView(GenericView):
    queryset = Scholarship.objects.all()
    serializer_class = ScholarshipSerializer
    cache_key_prefix = "scholarship"
    allowed_methods = ["list", "retrieve"]

class ManageScholarshipView(GenericView):
    queryset = Scholarship.objects.all()
    serializer_class = ScholarshipSerializer
    permission_classes = [IsAdminUser]
    cache_key_prefix = "manage-scholarship"
    allowed_methods = ["create", "update", "destroy"]

class InternshipView(GenericView):
    queryset = Internship.objects.all()
    serializer_class = InternshipSerializer
    cache_key_prefix = "internship"
    allowed_methods = ["list", "retrieve"]

class ManageInternshipView(GenericView):
    queryset = Internship.objects.all()
    serializer_class = InternshipSerializer
    permission_classes = [IsAdminUser]
    cache_key_prefix = "manage-internship"
    allowed_methods = ["create", "update", "destroy"]

class AnnouncementView(GenericView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
    cache_key_prefix = "announcement"
    allowed_methods = ["list", "retrieve"]

class ManageAnnouncementView(GenericView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
    permission_classes = [IsAdminUser]
    cache_key_prefix = "manage-announcement"

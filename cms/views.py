from main.utils.generic_api import GenericView
from .models import Article, Event, Scholarship, Internship, Announcement
from .serializers import ArticleSerializer, EventSerializer, ScholarshipSerializer, InternshipSerializer, AnnouncementSerializer
from rest_framework.permissions import IsAdminUser
class ArticleView(GenericView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    allowed_methods = ["list", "retrieve"]
    
class ManageArticleView(GenericView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAdminUser]
    allowed_methods = ["create", "update", "destroy"]

class EventView(GenericView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    allowed_methods = ["list", "retrieve"]

class ManageEventView(GenericView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAdminUser]
    allowed_methods = ["create", "update", "destroy"]

class ScholarshipView(GenericView):
    queryset = Scholarship.objects.all()
    serializer_class = ScholarshipSerializer
    allowed_methods = ["list", "retrieve"]

class ManageScholarshipView(GenericView):
    queryset = Scholarship.objects.all()
    serializer_class = ScholarshipSerializer
    permission_classes = [IsAdminUser]
    allowed_methods = ["create", "update", "destroy"]

class InternshipView(GenericView):
    queryset = Internship.objects.all()
    serializer_class = InternshipSerializer
    allowed_methods = ["list", "retrieve"]

class ManageInternshipView(GenericView):
    queryset = Internship.objects.all()
    serializer_class = InternshipSerializer
    permission_classes = [IsAdminUser]
    allowed_methods = ["create", "update", "destroy"]

class AnnouncementView(GenericView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
    allowed_methods = ["list", "retrieve"]

class ManageAnnouncementView(GenericView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
    permission_classes = [IsAdminUser]
    allowed_methods = ["create", "update", "destroy"]


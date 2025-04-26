from main.utils.generic_api import GenericView
from .models import Article, Event, Scholarship, Internship, Announcement
from .serializers import ArticleSerializer, EventSerializer, ScholarshipSerializer, InternshipSerializer, AnnouncementSerializer
from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView
from rest_framework.response import Response

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

class DashboardView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        events = Event.objects.all()
        scholarships = Scholarship.objects.all()
        internships = Internship.objects.all()
        announcements = Announcement.objects.all()
        
        event_count = events.count()
        scholarship_count = scholarships.count()
        internship_count = internships.count()
        announcement_count = announcements.count()
        
        most_recent_event = events.order_by('-date_created').first()
        most_recent_scholarship = scholarships.order_by('-opening_date').first()
        most_recent_internship = internships.order_by('-opening_date').first()
        most_recent_announcement = announcements.order_by('-date_created').first()
        
        return Response({
            "announcement": {
                "count": announcement_count,
                "most_recent": AnnouncementSerializer(most_recent_announcement).data
            },
            "event": {
                "count": event_count,
                "most_recent": EventSerializer(most_recent_event).data
            },
            "scholarship": {
                "count": scholarship_count,
                "most_recent": ScholarshipSerializer(most_recent_scholarship).data
            },
            "internship": {
                "count": internship_count,
                "most_recent": InternshipSerializer(most_recent_internship).data
            },
        })

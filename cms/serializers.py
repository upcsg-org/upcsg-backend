from rest_framework import serializers
from .models import Article, Event, Scholarship, Internship, Announcement

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    article = ArticleSerializer()

    class Meta:
        model = Event
        fields = '__all__'

class ScholarshipSerializer(serializers.ModelSerializer):
    article = ArticleSerializer()
    
    class Meta:
        model = Scholarship
        fields = '__all__'

class InternshipSerializer(serializers.ModelSerializer):
    article = ArticleSerializer()

    class Meta:
        model = Internship
        fields = '__all__'

class AnnouncementSerializer(serializers.ModelSerializer):
    article = ArticleSerializer()
    class Meta:
        model = Announcement
        fields = '__all__'

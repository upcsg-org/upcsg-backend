from rest_framework import serializers
from .models import Article, Event, Scholarship, Internship, Announcement

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    article = ArticleSerializer(required=False, allow_null=True)

    class Meta:
        model = Event
        fields = '__all__'
        
    def create(self, validated_data):
        article_data = validated_data.pop('article', None)
        
        if article_data:
            article = Article.objects.create(**article_data)
            event = Event.objects.create(article=article, **validated_data)
        else:
            event = Event.objects.create(**validated_data)
            
        return event
    
    def update(self, instance, validated_data):
        article_data = validated_data.pop('article', None)

        # Update the Event instance
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        # Manually update nested article
        if article_data and instance.article:
            for attr, value in article_data.items():
                setattr(instance.article, attr, value)
            instance.article.save()

        return instance

class ScholarshipSerializer(serializers.ModelSerializer):
    article = ArticleSerializer(required=False, allow_null=True)
    
    class Meta:
        model = Scholarship
        fields = '__all__'
        
    def create(self, validated_data):
        article_data = validated_data.pop('article', None)
        
        if article_data:
            article = Article.objects.create(**article_data)
            scholarship = Scholarship.objects.create(article=article, **validated_data)
        else:
            scholarship = Scholarship.objects.create(**validated_data)
            
        return scholarship

class InternshipSerializer(serializers.ModelSerializer):
    article = ArticleSerializer(required=False, allow_null=True)

    class Meta:
        model = Internship
        fields = '__all__'
        
    def create(self, validated_data):
        article_data = validated_data.pop('article', None)
        
        if article_data:
            article = Article.objects.create(**article_data)
            internship = Internship.objects.create(article=article, **validated_data)
        else:
            internship = Internship.objects.create(**validated_data)
            
        return internship

class AnnouncementSerializer(serializers.ModelSerializer):
    article = ArticleSerializer(required=False, allow_null=True)
    
    class Meta:
        model = Announcement
        fields = '__all__'
        
    def create(self, validated_data):
        article_data = validated_data.pop('article', None)
        
        if article_data:
            article = Article.objects.create(**article_data)
            announcement = Announcement.objects.create(article=article, **validated_data)
        else:
            announcement = Announcement.objects.create(**validated_data)
            
        return announcement

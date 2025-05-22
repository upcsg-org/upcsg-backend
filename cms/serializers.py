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

        # Update event fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        # If article_data is None, remove the article
        if article_data is None and instance.article:
            instance.article.delete()
            instance.article = None
            instance.save()

        # If article_data exists and article exists, update it
        elif article_data and instance.article:
            for attr, value in article_data.items():
                setattr(instance.article, attr, value)
            instance.article.save()

        # If article_data exists and no article exists, create it
        elif article_data and not instance.article:
            article = Article.objects.create(**article_data)
            instance.article = article
            instance.save()

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
    
    def update(self, instance, validated_data):
        article_data = validated_data.pop('article', None)

        # Update event fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        # If article_data is None, remove the article
        if article_data is None and instance.article:
            instance.article.delete()
            instance.article = None
            instance.save()

        # If article_data exists and article exists, update it
        elif article_data and instance.article:
            for attr, value in article_data.items():
                setattr(instance.article, attr, value)
            instance.article.save()

        # If article_data exists and no article exists, create it
        elif article_data and not instance.article:
            article = Article.objects.create(**article_data)
            instance.article = article
            instance.save()

        return instance

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
    
    def update(self, instance, validated_data):
        article_data = validated_data.pop('article', None)

        # Update event fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        # If article_data is None, remove the article
        if article_data is None and instance.article:
            instance.article.delete()
            instance.article = None
            instance.save()

        # If article_data exists and article exists, update it
        elif article_data and instance.article:
            for attr, value in article_data.items():
                setattr(instance.article, attr, value)
            instance.article.save()

        # If article_data exists and no article exists, create it
        elif article_data and not instance.article:
            article = Article.objects.create(**article_data)
            instance.article = article
            instance.save()

        return instance

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

    def update(self, instance, validated_data):
        article_data = validated_data.pop('article', None)

        # Update event fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        # If article_data is None, remove the article
        if article_data is None and instance.article:
            instance.article.delete()
            instance.article = None
            instance.save()

        # If article_data exists and article exists, update it
        elif article_data and instance.article:
            for attr, value in article_data.items():
                setattr(instance.article, attr, value)
            instance.article.save()

        # If article_data exists and no article exists, create it
        elif article_data and not instance.article:
            article = Article.objects.create(**article_data)
            instance.article = article
            instance.save()

        return instance
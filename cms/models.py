from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    body = models.TextField()
    author = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.title

class Event(models.Model):
    title = models.CharField(max_length=200)
    image_url = models.URLField(max_length=1000, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=True, blank=True)
    external_url = models.URLField(max_length=1000, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    body = models.TextField()

class Scholarship(models.Model):
    title = models.CharField(max_length=200)
    image_url = models.URLField(max_length=1000, null=True, blank=True)
    opening_date = models.DateField(null=True, blank=True)
    deadline = models.DateField(null=True, blank=True)
    requirements = models.TextField(null=True, blank=True)
    benefits = models.TextField(null=True, blank=True)
    organization = models.CharField(max_length=200, null=True, blank=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=True, blank=True)
    external_url = models.URLField(max_length=1000, null=True, blank=True)
    
    def __str__(self):
        return self.title
    
class Internship(models.Model):
    title = models.CharField(max_length=200)
    image_url = models.URLField(max_length=1000, null=True, blank=True)
    organization = models.CharField(max_length=200)
    requirements = models.TextField()
    benefits = models.TextField()
    opening_date = models.DateField(null=True, blank=True)
    deadline = models.DateField(null=True, blank=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=True, blank=True)
    external_url = models.URLField(max_length=1000, null=True, blank=True)
    
    def __str__(self):
        return self.title
    
class Announcement(models.Model):
    title = models.CharField(max_length=200)
    image_url = models.URLField(max_length=1000, null=True, blank=True)
    summary = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=True, blank=True)
    external_url = models.URLField(max_length=1000, null=True, blank=True)
    
    def __str__(self):
        return self.title

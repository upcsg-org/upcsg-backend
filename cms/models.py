from django.db import models

class Article(models.Model):
    """
    General Article model
    """

    title = models.CharField()
    date_created = models.DateTimeField(auto_now_add=True)
    body = models.CharField()
    author_first_name = models.CharField()
    author_last_name = models.CharField()
    email = models.CharField()
    job_title = models.CharField()

    def __str__(self):
        return f"{self.title} Article"
    
class Content(models.Model):
    """
    General Content model
    """

    image_url = models.CharField()
    datetime_created = models.DateTimeField(auto_now_add=True)
    title = models.CharField()
    external_url = models.CharField()

    def __str__(self):
        return f"{self.title} Content"

class Event(Content):
    """
    Event model
    """

    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    article = models.ForeignKey(Article, related_name='events')

    def __str__(self):
        return f"{self.title} Event"
    
class Announcement(models.Model):
    """
    Announcement model
    """

    summary = models.CharField()
    article = models.ForeignKey(Article, related_name='announcements')

    def __str__(self):
        return f"{self.title} Announcement"    
    
class Scholarship(Content):
    """
    Schalarship model
    """

    opening_date = models.DateField()
    deadline = models.DateField()
    requirements = models.JSONField()
    benefits = models.JSONField()
    organization = models.CharField()
    article = models.ForeignKey(Article, related_name='scholarships')

    def __str__(self):
        return f"{self.title} Scholarship"
    
class Internship(Content):
    """
    Internship model
    """

    opening_date = models.DateField()
    deadline = models.DateField()
    organization = models.CharField()
    requirements = models.JSONField()
    benefits = models.JSONField()
    article = models.ForeignKey(Article, related_name='internships')

    def __str__(self):
        return f"{self.title} Internship"

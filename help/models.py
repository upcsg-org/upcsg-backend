from django.db import models

class Concern(models.Model):
    class Status(models.TextChoices):
        PENDING = 'pending'
        RESOLVED = 'resolved'
        CLOSED = 'closed'
        
    name = models.CharField(max_length=255)
    email = models.TextField()
    content = models.TextField()
    status = models.CharField(max_length=255, choices=Status.choices, default=Status.PENDING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

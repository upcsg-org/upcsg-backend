from django.db import models

# Create your models here.

class Term(models.Model):
    startYear = models.IntegerField()
    endYear = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Term {self.startYear}-{self.endYear}"

class Officer(models.Model):
    term = models.ForeignKey(Term, on_delete=models.CASCADE, related_name='officers')
    image_url = models.URLField(null=True, blank=True)
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    yearlevel = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.position}"

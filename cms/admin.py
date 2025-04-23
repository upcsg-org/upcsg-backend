from django.contrib import admin
from .models import Article, Event, Scholarship, Internship, Announcement

admin.site.register(Article)
admin.site.register(Event)
admin.site.register(Scholarship)
admin.site.register(Internship)
admin.site.register(Announcement)

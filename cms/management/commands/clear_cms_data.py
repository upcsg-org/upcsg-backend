from django.core.management.base import BaseCommand
from cms.models import Article, Event, Scholarship, Internship, Announcement

class Command(BaseCommand):
    help = 'Clears all content-related data from the database'

    def handle(self, *args, **kwargs):
        self.stdout.write('Starting to clear content data...')

        # Delete dependent models first (they depend on Article)
        Announcement.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Deleted all announcements'))

        Internship.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Deleted all internships'))

        Scholarship.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Deleted all scholarships'))

        Event.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Deleted all events'))

        Article.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Deleted all articles'))

        self.stdout.write(self.style.SUCCESS('Successfully cleared all content data!'))

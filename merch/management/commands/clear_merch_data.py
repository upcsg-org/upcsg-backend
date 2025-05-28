from django.core.management.base import BaseCommand
from merch.models import MerchType, MerchSize, Merch, MerchVariant, Bundle

class Command(BaseCommand):
    help = 'Clears all merch data from the database'

    def handle(self, *args, **kwargs):
        self.stdout.write('Starting to clear merch data...')

        # Delete in reverse order of dependencies
        MerchVariant.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Deleted all merch variants'))

        Bundle.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Deleted all bundles'))

        Merch.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Deleted all merch items'))

        MerchSize.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Deleted all merch sizes'))

        MerchType.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Deleted all merch types'))

        self.stdout.write(self.style.SUCCESS('Successfully cleared all merch data!')) 
from django.core.management.base import BaseCommand
from merch.models import MerchType, MerchSize

class Command(BaseCommand):
    help = 'Populates initial merch types and sizes'

    def handle(self, *args, **kwargs):
        self.stdout.write('Starting to populate merch types and sizes...')

        # Create merch types
        merch_types = {
            'T-Shirts': 'UP Computer Science Guild T-Shirts',
            'Hats': 'UP Computer Science Guild Hats',
            'Bags': 'UP Computer Science Guild Bags'
        }

        created_types = {}
        for name, description in merch_types.items():
            merch_type, created = MerchType.objects.get_or_create(
                name=name,
                defaults={'description': description}
            )
            created_types[name] = merch_type
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created merch type: {name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Merch type already exists: {name}'))

        # Define sizes for each type
        sizes_data = {
            'T-Shirts': [
                ('Small', 'Small size for shirts'),
                ('Medium', 'Medium size for shirts'),
                ('Large', 'Large size for shirts'),
                ('XL', 'Extra Large size for shirts'),
            ],
            'Hats': [
                ('Small', 'Small size for hats'),
                ('Medium', 'Medium size for hats'),
                ('Large', 'Large size for hats'),
            ],
            'Bags': [
                ('Small', 'Small size for bags'),
                ('Medium', 'Medium size for bags'),
                ('Large', 'Large size for bags'),
            ]
        }

        # Create sizes for each type
        for type_name, sizes in sizes_data.items():
            merch_type = created_types[type_name]
            for name, description in sizes:
                size, created = MerchSize.objects.get_or_create(
                    merch_type=merch_type,
                    name=name,
                    defaults={'description': description}
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f'Created size: {name} for {type_name}'))
                else:
                    self.stdout.write(self.style.WARNING(f'Size already exists: {name} for {type_name}'))

        self.stdout.write(self.style.SUCCESS('Successfully populated merch types and sizes')) 
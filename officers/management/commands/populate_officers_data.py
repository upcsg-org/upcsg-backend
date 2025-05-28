from django.core.management.base import BaseCommand
from officers.models import Term, Officer

class Command(BaseCommand):
    help = 'Populates initial terms and officers data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Starting to populate terms and officers data...')

        # Create terms
        terms_data = [
            {
                'startYear': 2023,
                'endYear': 2024,
                'officers': [
                    {
                        'name': 'John Doe',
                        'position': 'President',
                        'yearlevel': '4th Year',
                        'image_url': 'https://example.com/president.jpg'
                    },
                    {
                        'name': 'Jane Smith',
                        'position': 'Vice President',
                        'yearlevel': '4th Year',
                        'image_url': 'https://example.com/vp.jpg'
                    },
                    {
                        'name': 'Mike Johnson',
                        'position': 'Secretary',
                        'yearlevel': '3rd Year',
                        'image_url': 'https://example.com/secretary.jpg'
                    }
                ]
            },
            {
                'startYear': 2022,
                'endYear': 2023,
                'officers': [
                    {
                        'name': 'Sarah Wilson',
                        'position': 'President',
                        'yearlevel': '4th Year',
                        'image_url': 'https://example.com/prev-president.jpg'
                    },
                    {
                        'name': 'Tom Brown',
                        'position': 'Vice President',
                        'yearlevel': '4th Year',
                        'image_url': 'https://example.com/prev-vp.jpg'
                    }
                ]
            }
        ]

        # Create terms and their officers
        for term_data in terms_data:
            term, created = Term.objects.get_or_create(
                startYear=term_data['startYear'],
                endYear=term_data['endYear']
            )
            
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created term: {term.startYear}-{term.endYear}'))
            else:
                self.stdout.write(self.style.WARNING(f'Term already exists: {term.startYear}-{term.endYear}'))

            # Create officers for this term
            for officer_data in term_data['officers']:
                officer, created = Officer.objects.get_or_create(
                    term=term,
                    name=officer_data['name'],
                    defaults={
                        'position': officer_data['position'],
                        'yearlevel': officer_data['yearlevel'],
                        'image_url': officer_data['image_url']
                    }
                )
                
                if created:
                    self.stdout.write(self.style.SUCCESS(f'Created officer: {officer.name} ({officer.position})'))
                else:
                    self.stdout.write(self.style.WARNING(f'Officer already exists: {officer.name} ({officer.position})'))

        self.stdout.write(self.style.SUCCESS('Successfully populated terms and officers data')) 
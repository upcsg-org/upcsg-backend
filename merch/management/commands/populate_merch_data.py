from django.core.management.base import BaseCommand
from merch.models import MerchType, MerchSize, Merch, MerchVariant
from decimal import Decimal

class Command(BaseCommand):
    help = 'Populates initial merch types, sizes, and products'

    def handle(self, *args, **kwargs):
        self.stdout.write('Starting to populate merch data...')

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
        created_sizes = {}
        for type_name, sizes in sizes_data.items():
            merch_type = created_types[type_name]
            created_sizes[type_name] = {}
            
            for size_name, description in sizes:
                size, created = MerchSize.objects.get_or_create(
                    name=size_name,
                    merch_type=merch_type,
                    defaults={'description': description}
                )
                created_sizes[type_name][size_name] = size
                if created:
                    self.stdout.write(self.style.SUCCESS(f'Created size: {size_name} for {type_name}'))
                else:
                    self.stdout.write(self.style.WARNING(f'Size already exists: {size_name} for {type_name}'))

        # Define merch items
        merch_items = {
            'T-Shirts': [
                {
                    'name': 'UPCSG Classic Tee',
                    'description': 'Classic black t-shirt with UPCSG logo',
                    'image': 'https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?w=800&auto=format&fit=crop&q=60',
                    'variants': [
                        {
                            'name': 'Black',
                            'price': Decimal('450.00'),
                            'variant': 'Black',
                            'is_bestseller': True,
                            'quantity': 50,
                            'image': 'https://images.unsplash.com/photo-1583743814966-8936f5b7be1a?w=800&auto=format&fit=crop&q=60',
                            'sizes': ['Small', 'Medium', 'Large', 'XL']
                        },
                        {
                            'name': 'White',
                            'price': Decimal('450.00'),
                            'variant': 'White',
                            'is_bestseller': False,
                            'quantity': 50,
                            'image': 'https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?w=800&auto=format&fit=crop&q=60',
                            'sizes': ['Small', 'Medium', 'Large', 'XL']
                        }
                    ]
                },
                {
                    'name': 'UPCSG Code Master Tee',
                    'description': 'T-shirt with coding-themed design',
                    'image': 'https://images.unsplash.com/photo-1583743814966-8936f5b7be1a?w=800&auto=format&fit=crop&q=60',
                    'variants': [
                        {
                            'name': 'Navy Blue',
                            'price': Decimal('500.00'),
                            'variant': 'Navy Blue',
                            'is_bestseller': True,
                            'quantity': 30,
                            'image': 'https://images.unsplash.com/photo-1583743814966-8936f5b7be1a?w=800&auto=format&fit=crop&q=60',
                            'sizes': ['Small', 'Medium', 'Large', 'XL']
                        }
                    ]
                }
            ],
            'Hats': [
                {
                    'name': 'UPCSG Snapback',
                    'description': 'Classic snapback with UPCSG logo',
                    'image': 'https://images.unsplash.com/photo-1588850561407-ed78c282e89b?w=800&auto=format&fit=crop&q=60',
                    'variants': [
                        {
                            'name': 'Black',
                            'price': Decimal('350.00'),
                            'variant': 'Black',
                            'is_bestseller': True,
                            'quantity': 40,
                            'image': 'https://images.unsplash.com/photo-1588850561407-ed78c282e89b?w=800&auto=format&fit=crop&q=60',
                            'sizes': ['Small', 'Medium', 'Large']
                        },
                        {
                            'name': 'Navy',
                            'price': Decimal('350.00'),
                            'variant': 'Navy',
                            'is_bestseller': False,
                            'quantity': 40,
                            'image': 'https://images.unsplash.com/photo-1588850561407-ed78c282e89b?w=800&auto=format&fit=crop&q=60',
                            'sizes': ['Small', 'Medium', 'Large']
                        }
                    ]
                }
            ],
            'Bags': [
                {
                    'name': 'UPCSG Laptop Bag',
                    'description': 'Stylish laptop bag with UPCSG branding',
                    'image': 'https://images.unsplash.com/photo-1548036328-c9fa89d128fa?w=800&auto=format&fit=crop&q=60',
                    'variants': [
                        {
                            'name': 'Black',
                            'price': Decimal('800.00'),
                            'variant': 'Black',
                            'is_bestseller': True,
                            'quantity': 20,
                            'image': 'https://images.unsplash.com/photo-1548036328-c9fa89d128fa?w=800&auto=format&fit=crop&q=60',
                            'sizes': ['Small', 'Medium', 'Large']
                        }
                    ]
                }
            ]
        }

        # Create merch items and their variants
        for type_name, items in merch_items.items():
            merch_type = created_types[type_name]
            
            for item_data in items:
                merch, created = Merch.objects.get_or_create(
                    name=item_data['name'],
                    merch_type=merch_type,
                    defaults={
                        'description': item_data['description'],
                        'image': item_data['image']
                    }
                )
                
                if created:
                    self.stdout.write(self.style.SUCCESS(f'Created merch item: {item_data["name"]}'))
                else:
                    self.stdout.write(self.style.WARNING(f'Merch item already exists: {item_data["name"]}'))

                # Create variants for each color and size combination
                for variant_data in item_data['variants']:
                    for size_name in variant_data['sizes']:
                        size = created_sizes[type_name][size_name]
                        variant, created = MerchVariant.objects.get_or_create(
                            merch=merch,
                            size=size,
                            variant=variant_data['variant'],
                            defaults={
                                'name': variant_data['name'],
                                'price': variant_data['price'],
                                'image': variant_data['image'],
                                'is_bestseller': variant_data['is_bestseller'],
                                'quantity': variant_data['quantity']
                            }
                        )
                        
                        if created:
                            self.stdout.write(self.style.SUCCESS(
                                f'Created variant: {variant_data["name"]} ({size_name}) for {item_data["name"]}'
                            ))
                        else:
                            self.stdout.write(self.style.WARNING(
                                f'Variant already exists: {variant_data["name"]} ({size_name}) for {item_data["name"]}'
                            ))

        self.stdout.write(self.style.SUCCESS('Successfully populated all merch data!')) 
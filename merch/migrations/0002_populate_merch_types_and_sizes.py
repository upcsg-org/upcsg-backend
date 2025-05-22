from django.db import migrations

def populate_merch_types_and_sizes(apps, schema_editor):
    MerchType = apps.get_model('merch', 'MerchType')
    MerchSize = apps.get_model('merch', 'MerchSize')

    # Create merch types
    shirt_type = MerchType.objects.create(
        name='T-Shirts',
        description='UP Computer Science Guild T-Shirts'
    )
    
    hat_type = MerchType.objects.create(
        name='Hats',
        description='UP Computer Science Guild Hats'
    )
    
    bag_type = MerchType.objects.create(
        name='Bags',
        description='UP Computer Science Guild Bags'
    )

    # Create sizes for shirts
    shirt_sizes = [
        ('Small', 'Small size for shirts'),
        ('Medium', 'Medium size for shirts'),
        ('Large', 'Large size for shirts'),
        ('XL', 'Extra Large size for shirts'),
    ]

    for name, description in shirt_sizes:
        MerchSize.objects.create(
            merch_type=shirt_type,
            name=name,
            description=description
        )

    # Create sizes for hats
    hat_sizes = [
        ('Small', 'Small size for hats'),
        ('Medium', 'Medium size for hats'),
        ('Large', 'Large size for hats'),
    ]

    for name, description in hat_sizes:
        MerchSize.objects.create(
            merch_type=hat_type,
            name=name,
            description=description
        )

    # Create sizes for bags
    bag_sizes = [
        ('Small', 'Small size for bags'),
        ('Medium', 'Medium size for bags'),
        ('Large', 'Large size for bags'),
    ]

    for name, description in bag_sizes:
        MerchSize.objects.create(
            merch_type=bag_type,
            name=name,
            description=description
        )

def reverse_populate_merch_types_and_sizes(apps, schema_editor):
    MerchType = apps.get_model('merch', 'MerchType')
    MerchType.objects.all().delete()

class Migration(migrations.Migration):
    dependencies = [
        ('merch', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(
            populate_merch_types_and_sizes,
            reverse_populate_merch_types_and_sizes
        ),
    ] 
# Generated by Django 5.1 on 2025-05-29 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_alter_article_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='external_url',
            field=models.URLField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='announcement',
            name='image_url',
            field=models.URLField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='body',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='external_url',
            field=models.URLField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='image_url',
            field=models.URLField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='internship',
            name='external_url',
            field=models.URLField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='internship',
            name='image_url',
            field=models.URLField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='scholarship',
            name='external_url',
            field=models.URLField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='scholarship',
            name='image_url',
            field=models.URLField(blank=True, max_length=1000, null=True),
        ),
    ]

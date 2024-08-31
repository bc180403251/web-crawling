# Generated by Django 3.2.12 on 2024-08-30 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crawler', '0002_rename_contant_scrapeddata_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scrapeddata',
            name='content',
        ),
        migrations.AddField(
            model_name='scrapeddata',
            name='location',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='scrapeddata',
            name='price',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='scrapeddata',
            name='property_categories',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='scrapeddata',
            name='property_images',
            field=models.JSONField(default=list),
        ),
        migrations.AddField(
            model_name='scrapeddata',
            name='property_size',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='scrapeddata',
            name='row',
            field=models.JSONField(null=True),
        ),
    ]
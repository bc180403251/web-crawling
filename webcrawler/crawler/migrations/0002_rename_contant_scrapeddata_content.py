# Generated by Django 3.2.12 on 2024-08-30 07:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crawler', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='scrapeddata',
            old_name='contant',
            new_name='content',
        ),
    ]
# Generated by Django 5.2.3 on 2025-06-20 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='timezone',
        ),
    ]

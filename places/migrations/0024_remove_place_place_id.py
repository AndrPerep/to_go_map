# Generated by Django 4.1.1 on 2023-03-07 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0023_place_place_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='place_id',
        ),
    ]

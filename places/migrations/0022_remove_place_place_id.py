# Generated by Django 4.1.1 on 2023-03-07 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0021_alter_place_short_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='place_id',
        ),
    ]
# Generated by Django 4.1.1 on 2022-10-29 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cityproject',
            name='description_short',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='cityproject',
            name='title',
            field=models.TextField(max_length=100),
        ),
    ]

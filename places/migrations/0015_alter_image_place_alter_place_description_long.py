# Generated by Django 4.1.1 on 2023-02-28 13:49

from django.db import migrations, models
import places.models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0014_remove_image_city_project_image_place_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='place',
            field=models.ForeignKey(on_delete=places.models.Place, related_name='images', to='places.place', verbose_name='место, с которым связано изображение'),
        ),
        migrations.AlterField(
            model_name='place',
            name='description_long',
            field=tinymce.models.HTMLField(blank=True, verbose_name='полное описание'),
        ),
    ]
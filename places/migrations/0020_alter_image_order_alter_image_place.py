# Generated by Django 4.1.1 on 2023-03-07 13:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0019_rename_description_long_place_long_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='order',
            field=models.PositiveIntegerField(blank=True, db_index=True, default=0, verbose_name='порядковый номер'),
        ),
        migrations.AlterField(
            model_name='image',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='places.place', verbose_name='место, с которым связано изображение'),
        ),
    ]

# Generated by Django 4.1.1 on 2023-02-11 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0011_alter_image_order_alter_image_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='order',
            field=models.PositiveIntegerField(db_index=True, default=0),
        ),
    ]

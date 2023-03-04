from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.TextField(max_length=100, verbose_name='Заголовок')
    place_id = models.TextField(max_length=50, blank=True, default='', verbose_name='id места')
    description_short = models.TextField(max_length=500, blank=True, default='', verbose_name='краткое описание')
    description_long = HTMLField(blank=True, verbose_name='полное описание')
    lng = models.FloatField(verbose_name='долгота')
    lat = models.FloatField(verbose_name='широта')

    def __str__(self):
        return self.title


class Image(models.Model):
    picture = models.ImageField(verbose_name='изображение')
    place = models.ForeignKey(
        'Place',
        Place,
        related_name='images',
        verbose_name='место, с которым связано изображение'
    )
    order = models.PositiveIntegerField(
        default=0,
        db_index=True,
        null=True,
        blank=True,
        verbose_name='порядковый номер'
    )

    class Meta:
        ordering = ['order']

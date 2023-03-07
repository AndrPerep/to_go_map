from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.TextField(max_length=100, verbose_name='Заголовок')
    short_description = models.TextField(max_length=500, blank=True, verbose_name='краткое описание')
    long_description = HTMLField(blank=True, verbose_name='полное описание')
    lng = models.FloatField(verbose_name='долгота')
    lat = models.FloatField(verbose_name='широта')

    def __str__(self):
        return self.title


class Image(models.Model):
    picture = models.ImageField(verbose_name='изображение')
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        related_name='images',
        verbose_name='место, с которым связано изображение',
    )
    order = models.PositiveIntegerField(
        default=0,
        db_index=True,
        blank=True,
        verbose_name='порядковый номер'
    )

    class Meta:
        ordering = ['order']

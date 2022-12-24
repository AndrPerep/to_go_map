from django.db import models
from tinymce.models import HTMLField


class CityProject(models.Model):
    title = models.TextField(max_length=100)
    place_id = models.TextField(max_length=50, blank=True, default='')
    description_short = models.TextField(max_length=500, blank=True, default='')
    description_long = HTMLField(null=True, blank=True)
    lng = models.FloatField()
    lat = models.FloatField()

    def __str__(self):
        return self.title


class Image(models.Model):
    picture = models.ImageField()
    city_project = models.ForeignKey(
        CityProject,
        related_name='images',
        on_delete=models.SET_NULL,
        null=True
    )
    order = models.PositiveIntegerField(
        default=0,
        db_index=True
    )

    class Meta:
        ordering = ['order']

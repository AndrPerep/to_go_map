from django.db import models


class CityProject(models.Model):
    title = models.TextField(max_length=100)
    description_short = models.TextField(max_length=500)
    description_long = models.TextField()
    lng = models.FloatField()
    lat = models.FloatField()

    def __str__(self):
        return self.title


class Image(models.Model):
    picture = models.ImageField()
    city_project = models.ForeignKey(
        CityProject,
        on_delete=models.SET_NULL,
        null=True
    )

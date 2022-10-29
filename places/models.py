from django.db import models


class CityProject(models.Model):
    title = models.TextField(max_length=100)
    description_short = models.TextField(max_length=500)
    description_long = models.TextField()
    lng = models.FloatField()
    lat = models.FloatField()


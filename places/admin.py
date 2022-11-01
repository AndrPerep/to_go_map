from django.contrib import admin
from places.models import CityProject, Image


@admin.register(CityProject)
class CityProjectAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'city_project']

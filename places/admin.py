from django.contrib import admin
from places.models import CityProject, Image


class ImageInline(admin.TabularInline):
    model = Image


@admin.register(CityProject)
class CityProjectAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = [ImageInline]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'city_project']


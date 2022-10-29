from django.contrib import admin
from places.models import CityProject


@admin.register(CityProject)
class CityProjectAdmin(admin.ModelAdmin):
    list_display = ['title']

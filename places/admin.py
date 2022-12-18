from django.contrib import admin
from places.models import CityProject, Image
from django.utils.html import format_html


class ImageInline(admin.TabularInline):
    model = Image
    readonly_fields = ['show_image']

    def show_image(self, obj):
        return format_html('<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.picture.url,
            width=obj.picture.width/(obj.picture.height/200),
            height=200,
        )
        )


@admin.register(CityProject)
class CityProjectAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = [ImageInline]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'city_project']
    fields = ['city_project']
    readonly_fields = ['show_image']

    def show_image(self, obj):
        return format_html('<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.picture.url,
            width=obj.picture.width/(obj.picture.height/200),
            height=200,
        )
        )


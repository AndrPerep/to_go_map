from django.contrib import admin
from places.models import Place, Image
from django.utils.html import format_html
from adminsortable2.admin import SortableAdminBase, SortableAdminMixin, SortableTabularInline


class ImageInline(SortableTabularInline):
    model = Image
    readonly_fields = ['show_image']

    list_display = ['picture', 'show_image', 'order']
    fields = ['show_image', 'order']

    def show_image(self, obj):
        return format_html('<img src="{url}" width="{width}" height={height} />',
            url=obj.picture.url,
            width=obj.picture.width/(obj.picture.height/200),
            height=200,
        )


@admin.register(Place)
class CityProjectAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [ImageInline]


@admin.register(Image)
class ImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['id', 'city_project', 'order']
    fields = ['city_project', 'picture']

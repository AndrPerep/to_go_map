from where_to_go.settings import MEDIA_ROOT

from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404

from places.models import CityProject, Image


def show_map(request):
    features = []
    for place in CityProject.objects.all():
        feature = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.lng, place.lat]
            },
            "properties": {
                "title": place.title,
                "placeId": "roofs24",
                "detailsUrl": "static/places/roofs24.json"
            }
        }
        features.append(feature)
    geo_data = {
        "geo_data": {
            "type": "FeatureCollection",
            "features": features
        }
    }
    return render(request, 'index.html', context=geo_data)


def show_place(request, place_id):
    place = get_object_or_404(CityProject, id=place_id)

    formated_place = {
        "title": place.title,
        "imgs": [MEDIA_ROOT + item.picture.url for item in place.images.all()],
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {
            "lng": place.lng,
            "lat": place.lat,
        },
        'aaa': MEDIA_ROOT
    }

    return JsonResponse(formated_place, json_dumps_params={'indent': 2, 'ensure_ascii': False})

from where_to_go.settings import MEDIA_ROOT

from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from places.models import CityProject


def get_place_details(place):
    formated_place = {
        "title": place.title,
        "imgs": [MEDIA_ROOT + item.picture.url for item in place.images.all()],
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {
            "lng": place.lng,
            "lat": place.lat,
        },
    }
    from pprint import pprint
    pprint(formated_place)
    return formated_place


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
                "detailsUrl": reverse(
                    'show_place_name', args=[place.id], current_app='places'
                )
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


def show_place(request=None, place_id=1):
    place = get_object_or_404(CityProject, id=place_id)

    print(place.images.all()[1].picture.url)

    formated_place = {
        "title": place.title,
        "imgs": [item.picture.url for item in place.images.all()],
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {
            "lng": place.lng,
            "lat": place.lat,
        },
    }

    return JsonResponse(formated_place, json_dumps_params={'indent': 2, 'ensure_ascii': False})

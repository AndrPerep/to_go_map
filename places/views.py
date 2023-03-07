from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from places.models import Place


def show_map(request):
    features = []

    for place in Place.objects.all():
        feature = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.lng, place.lat]
            },
            "properties": {
                "title": place.title,
                "detailsUrl": reverse(
                    show_place,
                    kwargs={'place_id': place.id},
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


def show_place(request, place_id=1):
    place = get_object_or_404(Place, id=place_id)

    formatted_place = {
        "title": place.title,
        "imgs": [item.picture.url for item in place.images.all()],
        "short_description": place.short_description,
        "long_description": place.long_description,
        "coordinates": {
            "lng": place.lng,
            "lat": place.lat,
        },
    }

    return JsonResponse(formatted_place, json_dumps_params={'indent': 2, 'ensure_ascii': False})

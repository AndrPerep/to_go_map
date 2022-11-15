from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from places.models import CityProject


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

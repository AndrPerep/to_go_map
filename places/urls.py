from . import views
from django.urls import path

urlpatterns = [
    path('', views.show_map),
    path('places/<int:place_id>/', views.show_place, name='show_place'),
]

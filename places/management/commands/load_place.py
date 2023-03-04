import os
import requests
import json
import logging

from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from django.core.exceptions import MultipleObjectsReturned
from places.models import Place, Image


class Command(BaseCommand):
    help = 'Загружает данные JSON с указанного адреса'

    def add_arguments(self, parser):
        parser.add_argument(
            '-address',
            '--a',
            type=str,
            help='Адрес с источником данных',
            dest='address'
        ),
        parser.add_argument(
            '-directory',
            '--d',
            type=str,
            help='Локальный адрес папки с файлами json',
            dest='directory'
        )

    def load_to_database(self, place_data):
        obj, created = Place.objects.get_or_create(
            title=place_data['title'],
            defaults={
                'description_short': place_data['description_short'],
                'description_long': place_data['description_long'],
                'lng': place_data['coordinates']['lng'],
                'lat': place_data['coordinates']['lat'],
            },
        )
        if created:
            for number, image_url in enumerate(place_data['imgs']):
                img_response = requests.get(image_url)
                img_response.raise_for_status()

                picture = ContentFile(img_response.content, name=f"{place_data['title']} ({number}).jpg")
                Image.objects.get_or_create(
                    order=number,
                    place=obj,
                    picture=picture
                )


    def handle(self, *args, **options):
        address = options['address']
        directory = options['directory']
        try:
            if address:
                response = requests.get(address)
                response.raise_for_status()
                self.load_to_database(response.json())
            if directory:
                files = [os.path.join(directory, filename) for filename in os.listdir(directory)]
                for filepath in files:
                    with open(filepath, 'r', encoding='utf-8') as file:
                        self.load_to_database(json.load(file))
        except MultipleObjectsReturned:
            logging.exception('Дубликаты в базе данных')
        except [requests.exceptions.ConnectionError, requests.exceptions.HTTPError]:
            logging.exception('Проблемы при загрузке данных')

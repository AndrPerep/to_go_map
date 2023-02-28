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

    def load_to_database(self, json_address):
        obj, created = Place.objects.get_or_create(
            title=json_address['title'],
            description_short=json_address['description_short'],
            description_long=json_address['description_long'],
            lng=json_address['coordinates']['lng'],
            lat=json_address['coordinates']['lat'],
        )
        if created:
            for number, image_url in enumerate(json_address['imgs']):
                img_response = requests.get(image_url)
                img_response.raise_for_status()

                picture = ContentFile(img_response.content, name=f"{json_address['title']} ({number}).jpg")
                Image.objects.get_or_create(
                    order=number,
                    city_project=obj,
                    picture=picture
                )


    def handle(self, *args, **options):
        address = options['address']
        if address:
            try:
                response = requests.get(address)
                response.raise_for_status()
                self.load_to_database(response.json())
            except MultipleObjectsReturned:
                logging.exception('Дубликаты в базе данных')
            except [requests.exceptions.ConnectionError, requests.exceptions.HTTPError]:
                logging.exception('Проблемы при загрузке данных')

        directory = options['directory']
        if directory:
            files = [os.path.join(directory, filename) for filename in os.listdir(directory)]
            try:
                for filepath in files:
                    with open(filepath, 'r', encoding='utf-8') as file:
                        self.load_to_database(json.load(file))
            except MultipleObjectsReturned:
                logging.exception('Дубликаты в базе данных')
            except [requests.exceptions.ConnectionError, requests.exceptions.HTTPError]:
                logging.exception('Проблемы при загрузке данных')

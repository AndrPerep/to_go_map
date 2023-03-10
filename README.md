# Куда пойти — Карта мест

Cайт о самых интересных местах в городе. [Демка сайта](http://parampamk.pythonanywhere.com/)

![&#x41A;&#x443;&#x434;&#x430; &#x43F;&#x43E;&#x439;&#x442;&#x438;](static_src/site.png)

## Как запустить

* Установка библиотек:
```commandline
    pip install -r requirements.txt
```
* Определение переменных окружения в файле `.env`, лежащем в корне проекта:
```dotenv
    DEBUG=False #режим отладки Django
    SECRET_KEY=secret_key #секретный ключ Django
    ALLOWED_HOSTS=[https://127.0.0.1, https://site.com] #список разрешённых адресов для сайта
```
* Запуск веб-сервера Django:
```commandline
    py manage.py runserver
```
* В панели администрирования Django по адресу `./admin` можно управлять базой данных.
Доступны текстовый редактор для описания и удобное управление картинками.

## Загрузка данных на сайт
#### Формат данных
```
Каждый json-файл содержит данные об одном объекте в следующем формате:

```json
{
  // * – обязательное поле
  "title": "Заголовок", // *
  "imgs": [
    "Адрес, откуда будет загружена картинка",
    "https://example.com/picture.jpg"
  ],
  "short_description": "Короткое описание",
  "long_description": "Полное описание",
  "coordinates": {
    "lng": "37.5",  // * долгота
    "lat": "55.7" // * широта
  }
}
```
#### Команды для загрузки
Используйте один из вариантов загрузки данных о местах на сайт:
1) Укажите адрес json файла через аргумент `-a` (`-address`):
```commandline
    py manage.py load_place -a https://example.com/file.json
```
2) Загрузите сразу несколько объектов, разместив json файлы в одной папке 
и указав адрес папки через аргумент `-d` (`-directory`):
```commandline
    py manage.py load_place -d C:\users\User\Desktop\directory
```
## Настройки

Внизу справа на странице можно включить отладочный режим логгирования.

![debug mode](static_src//debug-option.png)

Настройки сохраняются в Local Storage браузера и не пропадают после обновления страницы. Чтобы сбросить настройки удалите ключи из Local Storage с помощью Chrome Dev Tools —&gt; Вкладка Application —&gt; Local Storage.

Если что-то работает не так, как ожидалось, то начните с включения отладочного режима логгирования.

<a href="#" id="data-sources"></a>

## Используемые библиотеки

* [Leaflet](https://leafletjs.com/) — отрисовка карты
* [loglevel](https://www.npmjs.com/package/loglevel) — для логгирования
* [Bootstrap](https://getbootstrap.com/) — CSS библиотека
* [Vue.js](https://ru.vuejs.org/) — реактивные шаблоны на фронтенде
* [admin-sortable2](https://django-admin-sortable2.readthedocs.io/en/latest/) — перетаскивание объектов в админке
* [environs](https://pypi.org/project/environs/#usage-with-django) — для переменых окружения

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).

Тестовые данные взяты с сайта [KudaGo](https://kudago.com).


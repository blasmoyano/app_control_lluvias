## APP Control de LLuvias

Permite registrar las lluvias precipitadas en un campo.

## Instalación y Requerimientos

python 3.7 - Django 3
```sh
$ cd app_control_lluvias
$ pip install -r requirements.txt
```

## Urls
* [Documentación API](http://localhost:8080/docs/)
* [Admin](http://localhost:8080/desarrollo/admin/)
* [Web](http://localhost:8080/desarrollo/campo/)
* [GET POST lluvia por campo](http://localhost:8080/desarrollo/lluvia/api/v1/crear_lluvia_campo/2)
    * ID del campo
* [GET promedio](http://localhost:8080/desarrollo/lluvia/api/v1/promedio?dias=1)
    * dias, requeridos
* [GET promedio](http://localhost:8080/desarrollo/lluvia/api/v1/promedio?dias=1)
    * milimetros, requeridos

## Run

Setting:
* desarrollo
* produccion


```sh
$ python manage.py makemigrations [lluvias , campos] --settings=app_control_lluvias.settings.desarrollo
$ python manage.py migrate --settings=app_control_lluvias.settings.desarrollo
$ python manage.py runserver localhost:8080 --settings=app_control_lluvias.settings.desarrollo
```






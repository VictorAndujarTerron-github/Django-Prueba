# Django Pruebas

En este repositorio encontraréis un primer proyecto que he hecho con Django.

Aparte, utilizaré el propio [README](https://github.com/VictorAndujarTerron-github/Django-Prueba/new/main?filename=README.md) para explicar las cosas que he aprendido de Django mientras hacia el proyecto y también como he hecho.

## Crear entorno virtual
Si quieres trabajar con Django primero deberás instalar Python. Esto se debe a que Django es un *framework* de Python
Para empezar Django lo primero es crear nuestro entorno virtual. Para esto utilizaremos el siguiente comando:

- *python -m venv ...carpeta donde vas a guardar el entorno.../...nombre del entorno...*

Una vez creado deberemos de ponerlo en marcha. Para ello, entraremos en la carpeta donde tenemos guardado el entorno virtual y buscaremos la carpeta *bin*. En una terminal dentro de esta carpeta, lo activaremos con el comando:

- *source activate*

A partir de ahora, todos los comandos que ejecutemos en la terminal se estarán ejecutando dentro de ese entorno virtual.

## Instalar Django
Ahora sí que es el momento de instalar Django. Esto se hace con este comando:

- *pip install Django*

Con este comando instalamos la versión más reciente de Django. Si quisiéramos, también podríamos especificar cuál es la que nos interesa y pedirla. Aparte de instalarse Django, se instalan otras librerías que son necesarias para que funcione esa versión.

## Comando *django-admin --help*
Este comando es muy importante porque te permite ver cuáles son los subcomandos que nos permite ejecutar junto a django-admin (de este modo: *django-admin subcomando*). El subcomando que más nos interesa es el siguiente:

- *django-admin startproject ...nombre del projecto...*

Al ejecutar esto, se creará una nueva carpeta que será donde se guardara todo el proyecto. Dentro de ella hay otra carpeta y un archivo. La carpeta, que debe de tener el mismo nombre que el proyecto, contiene todas las configuraciones de este. El archivo, que se debe de llamar *manage.py*, sirve para ejecutar comandos, pero hacer que solo afecten a este proyecto.

## Ejecutar servidor
Si queremos ejecutar el servidor tendremos que entrar en la carpeta del proyecto. Dentro de esta carpeta ejecutaremos

- *python manage.py runserver*

Cuando lo ejecutes por primera vez te saldrá un error que no afecta a iniciar el servidor. Esto se solucionará en un punto más adelante de este Readme(**insertar enlace a migrations**).

## Modelo, Vista y Template (MVT)
Django nos permite crear apps dentro de un proyecto. Estas apps son las que utilizan el patrón MVT. Para crear una app dentro del proyecto hay que utilizar este comando:

- *python manage.py startapp ...nombre de la app...*

Una vez creada la app, se nos crea una nueva carpeta con el nombre de la aplicación. De todos los archivos que tiene esta carpeta, al principio nos vamos a centrar en estos:
- views.py
- models.py
También crearemos la carpeta *template* y como utilizarla.

## Creación del primer Modelo
Para crear nuestro primer modelo vamos a poner las siguientes líneas de código en el archivo models.py:

    from django.db import models

    # Create your models here.
    class Car(models.Model):
        title = models.TextField(max_length = 250)

En este caso hemos creado una clase/modelo de tipo coche con un único atributo que será el nombre del coche. "max_length" hace que número de caracteres que tiene el atributo es como máximo 250.

## Creando nuestro primer metodo en views
Las siguientes líneas de código:

    from django.shortcuts import render

    # Create your views here.
    def my_view(request):
        render(request, "my_first_app/car_list.html"

## Acknowledgements

 - [Curso de Django de Platzi](https://platzi.com/cursos/django/)
 - [README](README.md)

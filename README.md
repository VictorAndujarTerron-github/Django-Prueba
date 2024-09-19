# Django Pruebas

En este repositorio encontraréis un primer proyecto que he hecho con Django.

Aparte, utilizaré el propio [README](https://github.com/VictorAndujarTerron-github/Django-Prueba/blob/647eff8ac5a7e027aa511111adacf1fbc4d48512/README.md) para explicar las cosas que he aprendido de Django mientras hacia el proyecto y también como he hecho.

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

## Creando nuestro primer método en views
Las siguientes líneas de código:

    from django.shortcuts import render

    # Create your views here.
    def my_view(request):
        car_list = [
            {"title": "BMW"},
            {"title": "Nissan"},
            {"title": "Mazda"},
            {"title": "Tesla"}
        ]
        context = {
            "car_list": car_list
        }
    return render(request, "my_first_app/car_list.html", context)

El *context*, que es la lista de 4 coches que hemos creado, no nos es útil. Lo que de verdad necesitamos es que esta request acceda a la base de datos y nos pase los elementos de la tabla de coches. Esto se explica en otro punto más adelante del Readme (**insertar enlace a lectura de la base de datos**)

Para hacer que Django encuentre el archivo *car_list.html* tenemos que ir al archivo *settings.py* que estará en la carpeta con el mismo nombre del proyecto. En este archivo habrá que buscar la lista *INSTALLED APPS* y añadir ahí el nombre de nuestra aplicación.

## Creando nuestro primer template
Para crear un template, tenemos que tener una carpeta llamada *templates* y dentro de esta otra carpeta con el mismo nombre que el de la app que estamos creando. Ahí crearemos todos nuestros templates, en mi caso el primero se llamará car_list.html y contendrá el siguiente código:

    <html lang="en">
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>
            Car List
        </title>
    </head>
    <body>
        <h1>Esta es la lista de carros:</h1>
        {% for car in car_list %}
            <li>{{car.title}}</li>
        {% endfor %}
    </body>
    </html>

Este template es lo que se mostrará cuando un usuario haga click en un botón o link que tenga este asociado al "car_list.html", pero para ello tenemos que crear un path para que la app reconozca el template y lo pueda usar. Para ello, tenemos que buscar el archivo *"urls.py"* dentro de la carpeta de nuestro proyecto. Una vez encontrado, deberemos asociar la view que hemos creado anteriormente con un nuevo path, os debería de quedar así:

    from django.contrib import admin
    from django.urls import path
    from my_first_app.views import my_view

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('car-list/', my_view)
    ]

## Comprobación de lo hecho hasta ahora
Si queremos mirar si todo lo que hemos hecho hasta ahora funciona, debemos iniciar el servidor con la instrucción especificada más arriba. Si entramos al *http* que nos genera, nos saldrá error 404, ya que no es una página con dominio. Podemos ver que más abajo tenemos un listado de URLs, si copiamos la segunda (car-list/) junto a la dirección ip de nuestra web, deberíamos de ser capaces de ver el listado de coches que hemos creado antes.

## ORM
El ORM de Django nos permite crear clases en Python y relacionarlas con la base de datos y así evitar escribir sentencias SQL. Cada clase que creemos en Python se crea una tabla en la BD. Existe el término *migraciones*, estas se pueden correr desde los modelos hacia la BS y viceversa. 
- Si lo hacemos desde los modelos hacia la BD, todos los modelos que la BD no conociera los genera en forma de tablas.
- Si lo hacemos desde la BD hacia los modelos, podríamos eliminar una tabla de la BD.

Cada vez que modificamos algún modelo en el archivo *models.py*, habrá que hacer una migración desde los modelos hacia la BD.

## Migrate
Ahora vamos a solucionar el error que nos salía al iniciar el servidor. Este error nos especifica que hay 18 migraciones incompletas. Para migrar un modelo a la base de datos hay que usar el comando siguiente:

- *python manage.py migrate"

El problema es que esto no migra el modelo "Car". Para ello tenemos que poner el comando:

- *python manage.py makemigrations"

Que genera el modelo (se puede ver en el archivo recién creada) en del modelo, para luego usar:

- *python manage.py migrate"

Y así migrarla finalmente a la BD.

## Como ver la BD
Para poder ver la BD tenemos que ejecutar el comando:

- *./manage.py dbshell*

Este comando cambia la terminal para que pueda operar con la base de datos y entienda ordenes SQL. La base de datos en tu app se debe de llamar db.sqlite3.

Con el comando siguiente podremos ver todas las tablas que tiene la BD:

- *.table*

Ahí podremos ver el modelo que hemos creado identificado con el nombre de nuestra app seguido del nombre del modelo.

El comando:

- *scheme ...nombre de tabla...*

Permite saber como y con que atributos se identifica cada elemento de la tabla.

## Crear, editar y eliminar datos de la BD
Primero tenemos que ejecutar el siguiente comando para hacer que la terminal pueda operar con la BD como si el proyecto estuviera corriendo todo el rato:

- *python manage.py shell*

Cargamos el modelo en la shell con el comando:

- *from ...nombre de la app... import ...nombre del modelo...*

Para crear un nuevo dato en la base de datos tenemos que utilizar la siguiente línea de comandos:

- *...nombre del dato... = ...nombre del modelo...(...nombre del atributo...= ...valor del atributo, ...)*

Para poder ver los valores de un dato de un tipo de modelo en concreto tenemos que crear la siguiente función en el archivo models.py dentro de la declaración de ese modelo en concreto.

    # Este metodo imprime los datos que tenemos del objeto que llama a la función
    def __str__(self):
        return f"{self.title} - {self.year} - {self.color}"

Para finalmente guardar el dato en la BD tenemos que usar:

- *...nombre del dato... .save()*

Para cambiar un valor tenemos que hacer:

- *...nombre del dato... . ...nombre del atributo... = ...nuevo valor...*

Y luego hacer un save para que se registre el cambio en la BD.

Ya por último, para eliminar ejecutamos únicamente:

- *...nombre del dato... .delete()*

## Relaciones entre modelos
Aquí más adelante os dejo un ejemplo de código donde cada libro esta relacionado con una empresa o persona que lo publica:

    class Publisher(models.Model):
    name = models.TextField(max_length = 200)
    address = models.TextField(max_length = 200)

    # Este metodo imprime los datos que tenemos del objeto que llama a la función
    def __str__(self):
        return f"{self.name} - {self.address}"


    class Book(models.Model):
    title = models.TextField(max_length = 50)
    publication_date = models.DateField()
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)

En la línea en la que pone CASCADE hay tres configuraciones diferentes. Estas alteran lo que le pasara al dato Book en caso de que se elimine el Publisher con el que esta asociado, los valores son:

- DO_NOTHING --> no se hará ningun cambio en el dato si el Publisher se elimina.
- CASCADE --> se eliminará si el Publisher se elimina.
- PROTECT --> no permitira eliminar el Publisher ya que tiene asociaciones creadas.


## Acknowledgements

 - [Curso de Django de Platzi](https://platzi.com/cursos/django/)
 - [README](README.md)

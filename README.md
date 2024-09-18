# Django Pruebas

En este repositorio encontrareis un primer projecto que he hecho con Django.

A parte, utilizaré el propio [README](https://github.com/VictorAndujarTerron-github/Django-Prueba/new/main?filename=README.md) para resumir algunas de las cosas que he aprendido de Django mientras hacia el projecto.

## Crear entorno virtual
Si quieres trabajar con Django primero deberás instalar Python. Esto se debe a que Django es un *framework* de Python
Para empezar Django lo primero es crear nuestro entorno virtual. Para esto utilizaremos el siguiente comando:

- *python -m venv ...carpeta donde vas a guardar el entorno.../...nombre del entorno...*

Una vez creado deberemos de ponerlo en marcha. Para ello, entraremos en la carpeta donde tenemos guardado el entorno virtual y buscaremos la carpeta *bin*. En una terminal dentro de esta carpeta, lo activaremos con el comando:

- *source activate*

A partir de ahora, todos los comandos que ejecutemos en la terminal se estaran ejecutando dentro de ese entorno virtual.

## Instalar Django
Ahora si que es el momento de instalar Django. Esto se hace con este comando:

- *pip install Django*

Con este comando instalamos la versión más reciente de Django. Si quisieramos, también podriamos especificar cual es la que nos interesa y pedirla. A parte de instalarse Django, se installan otras librerias que son necesarias para que funcione esa versión.

## Comando *django-admin --help*
Este comando es muy importante porque te permite ver cuales son los subcomandos que nos permite ejecutar junto a django-admin (de este modo: *django-admin subcomando*). El subcomando que más nos interesa es el  siguiente:

- *django-admin startproject ...nombre del projecto...*

Al ejecutar esto, se creara una nueva carpeta que será donde se guardara todo el projecto. Dentro de ella hay otra carpeta y un archivo. La carpeta, que debe de tener el mismo nombre que el projecto, contiene todas las configuraciones de este. El archivo, que se debe de llamar *manage.py*, sirve para ejecutar comandos pero hacer que solo afecten a este projecto.

## Ejecutar servidor
Si queremos ejecutar el servidor tendremos que entrar en la carpeta del proyecto. Dentro de esta carpeta ejecutaremos

- *python manage.py runserver*

Cuando lo ejecutes por primera vez te saldrá un error que no afecta a iniciar el servidor. Esto se solucionara en un punto más adelante de este Readme(**insertar enlace a migrations**).

## Modelo, Vista y Template (MVT)
Django nos permite crear apps dentro de un projecto. Estas apps son las que utilizan el patrón MVT. Para crear una app dentro del projecto hay que utilizar este comando:

- *python manage.py startapp ...nombre de la app...*



## Acknowledgements

 - [Curso de Django de Platzi](https://platzi.com/cursos/django/)
 - [README](https://github.com/VictorAndujarTerron-github/Django-Prueba/new/main?filename=README.md)

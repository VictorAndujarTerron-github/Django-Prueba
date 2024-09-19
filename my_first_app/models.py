from django.db import models

# Create your models here.
class Car(models.Model):
    title = models.TextField(max_length = 250)
    year = models.TextField(max_length = 4, null=True)
    color = models.TextField(max_length = 25, null=True)

    # Este metodo imprime los datos que tenemos del objeto que llama a la función
    def __str__(self):
        return f"{self.title} - {self.year} - {self.color}"


class Publisher(models.Model):
    name = models.TextField(max_length = 200)
    address = models.TextField(max_length = 200)

    # Este metodo imprime los datos que tenemos del objeto que llama a la función
    def __str__(self):
        return f"{self.name} - {self.address}"


class Author(models.Model):
    name = models.TextField(max_length = 200)
    birthday = models.DateField()

    # Este metodo imprime los datos que tenemos del objeto que llama a la función
    def __str__(self):
        return f"{self.name}"


class Profile(models.Model):
    name = models.OneToOneField(Author, on_delete=models.CASCADE)
    website = models.URLField()
    biography = models.TextField(max_length = 500)

    def __str__(self):
        return f"{self.name}"


class Book(models.Model):
    title = models.TextField(max_length = 50)
    publication_date = models.DateField()
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    authors = models.ManyToManyField(Author, related_name="authors")

    # Este metodo imprime los datos que tenemos del objeto que llama a la función
    def __str__(self):
        return f"{self.title} - {self.publication_date}"
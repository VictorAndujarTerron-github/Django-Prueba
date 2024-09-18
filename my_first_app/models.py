from django.db import models

# Create your models here.
class Car(models.Model):
    title = models.TextField(max_length = 250)
    year = models.TextField(max_length = 4, null=True)
    color = models.models.TextField(max_length = 25, null=True)

    # Este metodo imprime los datos que tenemos del objeto que llama a la función
    def __str__(self):
        return f"{self.title} - {self.year} - {self.color}"
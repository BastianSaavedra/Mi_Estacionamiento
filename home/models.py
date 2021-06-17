from django.db import models

# Create your models here.
# Here's going to be the models of Mi Estacionamiento

request_options = [
    [0, "Consulta"],
    [1, "Sugerencia"],
    [2, "Reclamo"],
]

class Contact(models.Model):
    name = models.CharField('Nombre', max_length=100)
    last_name = models.CharField('Apellido', max_length=100)
    email = models.EmailField()
    type_request = models.IntegerField('Tipo de Solicitud', choices=request_options)
    message = models.TextField('Mensaje')

    def __str__(self):
        return self.email




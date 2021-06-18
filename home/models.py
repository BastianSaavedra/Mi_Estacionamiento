import geocoder
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

# Model Class Mapbox
mapbox_access_token = 'pk.eyJ1Ijoia2l6c2F3YSIsImEiOiJja3EwaTFjYnYwNTFuMm5xZzA4M3ZtNzhiIn0.jmj0NkJgDkqIgatSVz-wSw'

class Address(models.Model):
    direccion = models.CharField(max_length=500)
    lat = models.FloatField(blank=True, null=True)
    long = models.FloatField(blank=True, null=True)

    def save(self, *args, **kwargs):
        g = geocoder.mapbox(self.direccion, key=mapbox_access_token)
        g = g.latlng # [lat, long]
        self.lat = g[0]
        self.long = g[1]
        return super( Address, self).save(*args, **kwargs)

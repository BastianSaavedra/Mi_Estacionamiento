import geocoder
from django.db import models

# Create your models here.

mapbox_access_token = 'pk.eyJ1Ijoia2l6c2F3YSIsImEiOiJja3E3Mmhlc2swMjI1Mm91aHlybGI4dTl4In0.sW8qKEWwBNgrTyjT8TWDqQ'

type_home = [
    [0, "Casa"],
    [1, "Edificio"],
    [2, "Otro"]
]


class Address(models.Model):
    park_address = models.TextField('Direccion del Estacionamiento', null=True)
    specification = models.TextField('Especificacion del Estacionamiento', null=True)
    t_home = models.IntegerField('Tipo de Vivienda', choices=type_home, null=True)
    value = models.IntegerField('Valor Estacionamiento', default=0)
    available = models.BooleanField('Disponible', null=True)
    lat = models.FloatField(blank=True, null=True)
    long = models.FloatField(blank=True, null=True)

    def save(self, *args, **kwargs):
        g = geocoder.mapbox(self.park_address, key=mapbox_access_token)
        g = g.latlng # [lat, long]
        self.lat = g[0]
        self.long = g[1]
        return super(Address, self).save(*args, **kwargs)

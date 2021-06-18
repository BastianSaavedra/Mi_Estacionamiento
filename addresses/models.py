import geocoder
from django.db import models

# Create your models here.

# Model Class Mapbox

mapbox_access_token = 'pk.eyJ1Ijoia2l6c2F3YSIsImEiOiJja3EwaTFjYnYwNTFuMm5xZzA4M3ZtNzhiIn0.jmj0NkJgDkqIgatSVz-wSw'

class Address(models.Model):
    address = models.TextField()
    lat = models.FloatField(blank=True, null=True)
    long = models.FloatField(blank=True, null=True)

    def save(self, *args, **kwargs):
        g = geocoder.mapbox(self.address, key=mapbox_access_token)
        g = g.latlng # [lat, long]
        self.lat = g[0]
        self.long = g[1]
        return super( Address, self).save(*args, **kwargs)

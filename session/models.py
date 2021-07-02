from django.db import models
from django.contrib.auth.models import User
from creditcards.models import CardNumberField, CardExpiryField, SecurityCodeField

# Create your models here.


# CARD MODEL
class CardInformation(models.Model):
    cc_number = CardNumberField('Numero de Tarjeta')
    cc_expiry = CardExpiryField('Fecha de Expiracion')
    cc_code = SecurityCodeField('CVV')


# CARS MODEL => USER 
"""
patente
marca
modelo
year
color

"""
class CarsInformation(models.Model):
    car_patent = models.CharField('Placa Patente', max_length=10)
    car_brand = models.CharField('Marca del Auto', max_length=255)
    car_model = models.CharField('Modelo del Auto', max_length=255)
    car_year = models.DateField('Año del Auto')

class ChooseOptions(models.Model):
    choose_car = models.ForeignKey(CarsInformation, on_delete=models.CASCADE)
    choose_payment = models.ForeignKey(CardInformation, on_delete=models.CASCADE)






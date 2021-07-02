
from django.db import models
from creditcards.models import CardNumberField, CardExpiryField, SecurityCodeField 

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

class Payment(models.Model):
    cc_number = CardNumberField('Numero de Tarjeta')
    cc_expiry = CardExpiryField('Fecha de expiracion')
    cc_code = SecurityCodeField('CVV')
 


# OWNER MODEL

type_home = [
    [0, "Casa"],
    [1, "Edificio"],
    [2, "Otro"]
]

class Owner(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Nombre', max_length=255)
    last_name = models.CharField('Apellido', max_length=255)
    phone = models.CharField('Numero de telefono', max_length=255)
    email = models.EmailField() 
    address = models.TextField('Direccion', max_length=255)
    cc_number = CardNumberField('Numero de Tarjeta')
    cc_expiry = CardExpiryField('Fecha de Expiracion')
    cc_code = SecurityCodeField('CVV')
    type_home = models.IntegerField('Tipo de Vivienda', choices = type_home)
    park_address = models.TextField('Direccion del estacionamiento')
    password = models.CharField('Contraseña', max_length=255)
    objects = models.Manager()

    
# CLIENT MODEL

type_bank = [
    [0, "Banco Bice"], 
    [1, "Banco Central de Chile"], 
    [2, "Banco de Chile"], 
    [3, "Banco de Credito e Inversiones"], 
    [4, "Banco del Desarrollo"],
    [5, "Banco Edwards"], 
    [6, "Banco Falabella"], 
    [7, "Banco Santander"], 
    [8, "Banco Security"], 
    [9, "BancoEstado"],
    [10, "BBVA"],
    [11, "Santander Banefe"],
]

class Client(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Nombre', max_length=255)
    last_name = models.CharField('Apellido', max_length=255)
    phone = models.CharField('Numero de telefono', max_length=255)
    email = models.EmailField()
    address = models.TextField('Direccion', max_length=255)
    cc_number_client = CardNumberField('Numero de Tarjeta')
    cc_expiry_client = CardExpiryField('Fecha de Expiracion')
    cc_code_client = SecurityCodeField('CVV')
    #bank_account = models.IntegerField('Banco', choices=type_bank)
    car_patent = models.CharField('Patente', max_length=6)
    car_brand = models.CharField('Marca', max_length=255)
    car_model = models.CharField('Modelo del Auto', max_length=255)
    car_year = models.IntegerField('Año del Auto', null=True)
    car_color = models.CharField('Color del Auto', max_length=255)
    available = models.BooleanField('Disponible', null=True)
    objects = models.Manager()

    



# Generated by Django 3.2.3 on 2021-06-29 04:19

import creditcards.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_ownerinformation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, verbose_name='Nombre')),
                ('last_name', models.CharField(max_length=255, verbose_name='Apellido')),
                ('phone', models.CharField(max_length=255, verbose_name='Numero de telefono')),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField(max_length=255, verbose_name='Direccion')),
                ('cc_number', creditcards.models.CardNumberField(max_length=25, verbose_name='Numero de Tarjeta')),
                ('cc_expiry', creditcards.models.CardExpiryField(verbose_name='Fecha de Expiracion')),
                ('cc_code', creditcards.models.SecurityCodeField(max_length=4, verbose_name='CVV')),
                ('type_home', models.IntegerField(choices=[[0, 'Casa'], [1, 'Edificio'], [2, 'Otro']], verbose_name='Tipo de Vivienda')),
                ('park_address', models.TextField(verbose_name='Direccion del estacionamiento')),
                ('password', models.CharField(max_length=255, verbose_name='Contraseña')),
            ],
        ),
        migrations.DeleteModel(
            name='OwnerInformation',
        ),
    ]

from django.contrib import admin
from . import models 

# Register your models here.

admin.site.register(models.Contact)
admin.site.register(models.Payment)
admin.site.register(models.Owner)
admin.site.register(models.Client)

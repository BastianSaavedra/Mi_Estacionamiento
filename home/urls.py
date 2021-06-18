# Urls App Home

from django.contrib import admin
from django.urls import path, include
from .views import index, contact, AddressView 


urlpatterns = [
    path('', index, name="index-html"),
    path('contact/', contact, name="contact"),
    path('map/', AddressView.as_view(), name="map-box"),

]

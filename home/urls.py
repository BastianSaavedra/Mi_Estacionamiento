# Urls App Home

from django.contrib import admin
from django.urls import path, include
from .views import index, register, add_card


urlpatterns = [
    path('', index, name="index-html"),
    path('register-user/', register, name="register-user"),
    path('card/', add_card, name="user-card")

]

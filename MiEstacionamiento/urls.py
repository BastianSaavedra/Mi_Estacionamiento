"""MiEstacionamiento URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from home import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('session.urls')),
    path('social-auth/', include('social_django.urls', namespace='social')),
    path('', include('addresses.urls')),



    # Multi step form url's Owner
    path('multistepformexample', views.multistepformexample, name="multistepformexample"),
    path('multistepformexample_save', views.multistepformexample_save, name="multistepformexample_save"),

    # Multi step form ulr's Client
    path('multistepformexampleclient', views.multistepformexampleclient, name="multistepformexampleclient"),
    path('multistepformexampleclient_save', views.multistepformexampleclient_save, name="multistepformexampleclient_save" ),
]

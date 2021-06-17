from django.urls import path
from .views import AddressView


urlpatterns = [
        path('map-box/', AddressView.as_view(), name='map-box'),
            
]

from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Address
from django import forms

# Create your views here.

class AddressView(CreateView):
    
    model = Address
    fields = ['park_address']
    template_name = 'addresses/map.html'
    success_url = "/"
    widgets = {
        'direccion': forms.TextInput(attrs={'class': 'input'}),
    }


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mapbox_access_token'] = 'pk.eyJ1Ijoia2l6c2F3YSIsImEiOiJja3E3Mmhlc2swMjI1Mm91aHlybGI4dTl4In0.sW8qKEWwBNgrTyjT8TWDqQ'
        context['addresses'] = Address.objects.all()
        return context


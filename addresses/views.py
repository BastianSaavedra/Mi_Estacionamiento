from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Address

class AddressView(CreateView):
    model = Address
    fields = ['address']
    template_name = 'addresses/map.html'
    success_url = '/'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mapbox_access_token'] = 'pk.eyJ1Ijoia2l6c2F3YSIsImEiOiJja3EwaTFjYnYwNTFuMm5xZzA4M3ZtNzhiIn0.jmj0NkJgDkqIgatSVz-wSw'
        context['addresses'] = Address.objects.all()
        return context

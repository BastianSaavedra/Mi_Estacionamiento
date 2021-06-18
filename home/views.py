from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateUserForm, ContactForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.views.generic.edit import CreateView
from .models import Address

# Create your views here.

"""
    DEBO INGRESAR LAS VARIABLES DE LOS HTML'S COMO

    username = request.POST.get["variable creadad en index"]
"""
def index(request):
    data = {
        'form': CreateUserForm()
    }
    if request.method == "POST":
        formulario = CreateUserForm(
                data=request.POST
        )
        if formulario.is_valid():
            formulario.save()
            user = authenticate(
                    username = formulario.cleaned_data["username"],
                    password = formulario.cleaned_data["password1"],
            )
            login(
                request,
                user,
            )
            messages.success(
                request,
                "Su cuenta ha sido creada exitosamente!",
            )
            return redirect(to = "/")
        data["form"] = formulario
    return render(
        request,
        'mi_estacionamiento/index.html',
        data
    )

def contact(request):
    data = {
        'contact_form':ContactForm()
    }
    if request.method == "POST":
        form = ContactForm(
                data=request.POST,
            )
        if form.is_valid():
            form.save()
            messages.success(
                    request,
                    "Mensaje enviado exitosamente"
            )
        else:
            data["contact_form"] = form
    return render(
            request,
            'mi_estacionamiento/index.html',
            data
        )

# Class CreateView Address
class AddressView(CreateView):

    model = Address
    fields = ['address']
    template_name = 'mi_estacionamiento/index.html'
    success_url = 'index-html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mapbox_access_token'] = 'pk.eyJ1Ijoia2l6c2F3YSIsImEiOiJja3EwaTFjYnYwNTFuMm5xZzA4M3ZtNzhiIn0.jmj0NkJgDkqIgatSVz-wSw'
        context['addresses'] = Address.objects.all()
        return context

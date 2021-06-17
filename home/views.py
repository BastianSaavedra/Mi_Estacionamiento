from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateUserForm, ContactForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
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


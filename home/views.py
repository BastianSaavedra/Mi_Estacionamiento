from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateUserForm, ContactForm, PaymentForm
from django.contrib.auth import authenticate, login
from django.contrib import messages

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from .models import Owner, Client




# Create your views here.

"""
    DEBO INGRESAR LAS VARIABLES DE LOS HTML'S COMO

    username = request.POST.get["variable creadad en index"]
"""

def register(request):
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
        'registration/register.html',
        data
    )

def index(request):
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

def add_card(request):
    data = {
        'payment_form': PaymentForm()
    }
    if request.method == "POST":
        form = PaymentForm(
            data = request.POST,
        )
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Targeta agregada exitosamente"
            )
        else:
            data["payment_form"] = form
    return render(
        request,
        'user/card_user.html',
        data
    )

# VIEWS MULTI STEP HTML REGISTER
#
def multistepformexample(request):
    return render(
        request,
        "registration/multi_step_registration.html"
    )

def multistepformexample_save(request):
    if request.method!="POST":
        return HttpResponseRedirect(

            reverse("multistepformexample")
        )
    else:
        # Personal Information
        name = request.POST.get('name')
        last_name = request.POST.get('last_name')
        phone = request.POST.get('phone')
        
        # Address Details
        type_home = request.POST.get('type_home')
        address = request.POST.get('address')
        park_address = request.POST.get('park_address')

        # Credit card Details
        cc_number = request.POST.get('cc_number')
        cc_expiry = request.POST.get('cc_expiry')
        cc_code = request.POST.get('cc_code')
        
        # Account Information
        email = request.POST.get('email')
        password = request.POST.get('pass')
        cpass = request.POST.get('cpass')
        if password!=cpass:
            messages.error(request, "Contraseña de confirmacion no coincide")
            return HttpResponseRedirect(reverse('multistepformexample'))

        try:
            multistepform =  Owner(
                name=name,
                last_name=last_name,
                email=email,
                phone=phone,
                address=address,
                cc_number=cc_number,
                cc_expiry=cc_expiry,
                cc_code=cc_code,
                type_home=type_home,
                park_address=park_address,
                password=password,
            )
            multistepform.save()
            messages.success(request, "Registro guardado correctamente")
            return HttpResponseRedirect(reverse('multistepformexample'))
        except:
            messages.error(request, "Error al guardar el registro")
            return HttpResponseRedirect(reverse('multistepformexample'))


def multistepformexampleclient(request):
    return render(
        request,
        "registration/multi_step_registration_client.html"
    )

def multistepformexampleclient_save(request):
    pass

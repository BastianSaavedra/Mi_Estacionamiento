from django.contrib.auth import logout, login, authenticate
from django.http.response import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import OwnerRegisterForm, CardInformationForm, CarInformationForm
from django.views.generic import ListView
from .models import CardInformation, CarsInformation

def sidebar(request):
    return render(
        request,
        'user/sidebar_profile.html'
    )


def owner_register(request):
    data = {
        'owner_register_form': OwnerRegisterForm() 
    }
    if request.method == 'POST':
        form = OwnerRegisterForm(
            data=request.POST
        )
        if form.is_valid():
            form.save()
            user = authenticate(
                username = form.cleaned_data["username"],
                password = form.cleaned_data["password1"],
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
        data["owner_register_form"] = form
    return render(
        request,
        'registration/registro.html',
        data
    )

# LISTVIEW CREDIT CARD MODEL
class CardInformationListView(ListView):
    model = CardInformation
    template_name = 'user/card/card_list.html'

# LISTVIEW CARS
class CarsInformationListView(ListView):
    model = CarsInformation
    template_name = 'user/car/car_list.html'

# ADD A CREDIT CARD TO USER
def add_card(request):
    data = {
        'card_form' : CardInformationForm()
    }
    if request.method == 'POST':
        form = CardInformationForm(
            data = request.POST,
            files = request.FILES
        )
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Tarjeta de credito añadida exitosamente!"
            )
            return redirect(to="cards-list")
        return render(
            request,
            'user/card/add_card.html',
            data
        )
# UPDATE A CREDIT CARD
def update_card(request):
    card = get_object_or_404(CardInformation, id=id)
    data = {
        'card_form': CardInformationForm(instance=card)
    }
    if request.method == 'POST':
        form = CardInformationForm(
            data=request.POST,
            instance=card,
            files=request.FILES
        )
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "La tarjeta ha sido modificado exitosamente!"
            )
            return redirect(to="cards-list")
        data["card_form"] = form
    return render(
        request,
        "user/card/update_car.html",
        data
    )

# DELETE A CREDIT CARD
def delete_card(request, id):
    card = get_object_or_404(CardInformation, id=id)
    card.delete()
    messages.success(
        request,
        "La tarjeta ha sido eliminada exitosamente!"
    )
    return redirect(to="card-list")

# ADD A CAR TO USER
def add_car(request):
    data = {
        'car_form' : CarInformationForm()
    }
    if request.method == 'POST':
        form = CarInformationForm(
            data = request.POST,
            files = request.FILES
        )
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Auto añadido exitosamente!"
            )
            return redirect(to="car-list")
        return render(
            request,
            'user/car/add_car.html',
            data
        )

# UPDATE A CAR 
def update_car(request, id):
    car = get_object_or_404(CarsInformation, id=id)
    data = {
        'car_form' : CarInformationForm(instance=car)
    }
    if request.method == 'POST':
        form = CarInformationForm(
            data=request.POST,
            instance=car,
            files=request.FILES
        )
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "El automovil ha sido modificado exitosamente!"
            )
            return redirect(to="cars-list")
        data["car_form"] = form
    return render(
        request,
        'user/car/update_car.html',
        data
    )

# DELETE CAR
def delete_car(request, id):
    car = get_object_or_404(CarsInformation, id=id)
    car.delete()
    messages.success(
        request,
        "El automovil ha sido eliminado exitosamente!"
    )
    return redirect(to="cars-list")


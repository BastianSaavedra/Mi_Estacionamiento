from django.contrib.auth import logout, login, authenticate
from django.http.response import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.


def user_login(request):

    if request.method == 'POST':
        username = request.POST.get["username"]
        password = request.POST.get["password"]
        user = authenticate(
            request,
            username = username,
            password = password
        )
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect("index-html")
            else:
                return HttpResponse("<h1> Cuenta deshabilitada </h1>")
        else:
            return HttpResponse("<h1> Ingreso no exitoso </h1>")

        return render(
            request,
            "registration/login.html"
        )


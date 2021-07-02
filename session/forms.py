from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import CardInformation, CarsInformation
from django.forms import ModelForm

class OwnerRegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2',
        ]
    
class CardInformationForm(ModelForm):

    class Meta:
        model = CardInformation
        fields = ['cc_number', 'cc_expiry', 'cc_code']

class CarInformationForm(ModelForm):

    class Meta:
        model = CarsInformation
        fields = ['car_patent', 'car_brand', 'car_model', 'car_year']

        widgets = {
            'car_year': forms.SelectDateWidget(years=range(1990, 2021))
        }

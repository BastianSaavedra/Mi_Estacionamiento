
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from .models import Contact

class CreateUserForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ContactForm(ModelForm):

    class Meta:
        model = Contact
        fields = ['name', 'last_name', 'email', 'type_request', 'message']


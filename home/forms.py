
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from .models import Contact, Payment
from creditcards.forms import CardNumberField, CardExpiryField, SecurityCodeField

class CreateUserForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
                'username': forms.TextInput(attrs={'class': 'input'}),
                'email': forms.EmailInput(attrs={'class': 'input'}),
                'password1': forms.PasswordInput(attrs={'class': 'input'}),
                'password2': forms.PasswordInput(attrs={'class': 'input'}),
        }


class ContactForm(ModelForm):
    class Meta:
        model = Contact 
        fields = ['name', 'last_name', 'email', 'type_request', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input'}),
            'last_name': forms.TextInput(attrs={'class': 'input'}),
            'email': forms.EmailInput(attrs={'class': 'input'}),
            'type_request': forms.Select(attrs={'class': 'input' }),
            'message': forms.Textarea(attrs={'class': 'input'}),
        }

class PaymentForm(ModelForm):

    class Meta:
        model = Payment
        fields = ['cc_number', 'cc_expiry', 'cc_code']

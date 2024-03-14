from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms



class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=False)
    
    class Meta:
        Model = User
        fields = ['username', 'email', 'password1', 'password2']
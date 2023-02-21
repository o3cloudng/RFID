from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from .models import User


class UserForm(UserCreationForm):
    first_name = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control rounded', 'placeholder':'First name'}))
    last_name = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control rounded', 'placeholder':'Last name'}))
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control rounded', 'placeholder':'Email Address'}))
    phone_number = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control rounded', 'placeholder':'Phone number'}))
    password1 = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control rounded', 'placeholder':'Password','type':'password'}))
    password2 = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control rounded', 'placeholder':'Confirm Password','type':'password'}))

    class Meta:
        model = User
        fields = [
            'first_name', 
            'last_name', 
            'email',
            'phone_number',
            'password1', 
            'password2', 
            ]


class UserChangeForm(UserChangeForm):
    first_name = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control rounded', 'placeholder':'First name'}))
    last_name = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control rounded', 'placeholder':'Last name'}))
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control rounded', 'placeholder':'Email Address'}))
    
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]
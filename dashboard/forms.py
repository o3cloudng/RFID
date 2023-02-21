from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control rounded', 'placeholder':'Email Address'}))
    password = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control rounded', 'placeholder':'First name', 'type':'password'}))
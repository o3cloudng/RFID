from django import forms
from .models import Device


class DeviceForm(forms.ModelForm):

    location = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control rounded', 'placeholder':'Location'}))
    device_id = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control rounded', 'placeholder':'Device ID'}))
    description = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control rounded', 'placeholder':'Description'}))

    class Meta:
        model = Device
        fields = ['location','device_id','description']

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['firstname'].widget.attrs.update({'class': 'form-control'})
    #     self.fields['lastname'].widget.attrs.update({'class':'form-control'})

    # def clean_email(self):
    #     cleaned_data = self.cleaned_data
    #     print("Cleaned data: ", cleaned_data)
    #     email = cleaned_data.get("email")
    #     # print("Email: ", email)
    #     if email.lower().strip() == "":
    #         raise forms.ValidationError("Email cannot be empty.")
    #     return email

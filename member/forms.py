from django import forms
from phonenumber_field.modelfields import PhoneNumberField
from .models import Member


class MemberForm(forms.ModelForm):
    firstname = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control rounded', 'placeholder':'First name'}))
    lastname = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control rounded', 'placeholder':'Last name'}))
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control rounded', 'placeholder':'Email Address'}))
    phone_number = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control rounded', 'placeholder':'Phone number'}))
    parent_guardian = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control rounded', 'placeholder':'Parent or Guardian'}))
    tag_id = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control rounded', 'placeholder':'Tag ID'}))
    notify = forms.BooleanField(label="Notify", required=False)
    address = forms.CharField(label="", widget=forms.Textarea(attrs={"rows":"5", "class":"form-control rounded", 'placeholder':'Home Address'}))

    class Meta:
        model = Member
        fields = ['firstname','lastname','email','tag_id','phone_number','parent_guardian','notify','address']

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['firstname'].widget.attrs.update({'class': 'form-control'})
    #     self.fields['lastname'].widget.attrs.update({'class':'form-control'})

    def clean_email(self):
        cleaned_data = self.cleaned_data
        print("Cleaned data: ", cleaned_data)
        email = cleaned_data.get("email")
        # print("Email: ", email)
        if email.lower().strip() == "":
            raise forms.ValidationError("Email cannot be empty.")
        return email

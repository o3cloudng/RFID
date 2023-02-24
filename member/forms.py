from django import forms
from phonenumber_field.modelfields import PhoneNumberField
from .models import Member


class MemberForm(forms.ModelForm):
    SEX_CHOICES = [
        ('MALE', 'Male'),
        ('FEMALE', 'Female'),
    ]
    STATUS = (
        ('DAY', 'Day'),
        ('BOARDER', 'Boarder'),
    )

    tag_id = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control rounded', 'placeholder':'Tag ID'}))
    firstname = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control rounded', 'placeholder':'First name'}))
    lastname = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control rounded', 'placeholder':'Last name'}))
    day_boarder = forms.ChoiceField(label="", choices=STATUS, widget=forms.Select(attrs={'class':'form-control rounded', 'placeholder':'Day / Boarder'}))
    student_age = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control rounded', 'placeholder':"Student's Age"}))
    student_sex = forms.ChoiceField(label="", choices=SEX_CHOICES, widget=forms.Select(attrs={'class':'form-control rounded', 'placeholder':"Student's Gender"}))
    parent_guardian_name = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control rounded', 'placeholder':'Parent or Guardian name'}))
    parent_guardian_phone = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control rounded', 'placeholder':'Parent or Guardian Phone number'}))
    parent_guardian_email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control rounded', 'placeholder':'Parent or Guardian  Email Address'}))
    parent_guardian_address = forms.CharField(label="", widget=forms.Textarea(attrs={"rows":"5", "class":"form-control rounded", 'placeholder':'Parent or Guardian Address'}))
    notify = forms.BooleanField(label="Notify", required=False)
    # address = forms.CharField(label="", widget=forms.Textarea(attrs={"rows":"5", "class":"form-control rounded", 'placeholder':'Student Address'}))

    class Meta:
        model = Member
        fields = ['firstname','lastname','parent_guardian_name','tag_id','parent_guardian_phone','parent_guardian_email','parent_guardian_address','notify','day_boarder', 'student_age','student_sex']

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

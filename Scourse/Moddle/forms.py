from django import forms
from django.core import validators
from .models import lecturer
class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter your email again: ')
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']

        if email != vmail:
            raise forms.ValidationError("MAKE SURE EMAILS MATCH !")
class LecturerForm(forms.ModelForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    dob = forms.DateField()
    gender = forms.CharField()
    address = forms.CharField()
    phone = forms.CharField()
    email = forms.EmailField()
    Organization = forms.CharField()
    class Meta:
        model = lecturer
        fields=['first_name','last_name','dob','gender','address','phone','email','Organization']

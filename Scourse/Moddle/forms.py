from django import forms
from django.core import validators
from .models import lecturer,student,Course,HomeWork
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.utils import ValidationError


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

class EditCourseForm(forms.ModelForm):
    name = forms.CharField(max_length=100)
    starting_time = forms.DateField()
    ending_time = forms.DateField()
    class Meta:
        model = Course
        fields=['name','starting_time','ending_time']

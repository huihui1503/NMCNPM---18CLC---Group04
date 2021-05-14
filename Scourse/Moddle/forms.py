from django import forms
from django.core import validators
<<<<<<< HEAD
from .models import lecturer
from django.forms.widgets import NumberInput
class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter your email again: ')
    text = forms.CharField(widget=forms.Textarea)
=======
from .models import lecturer,student,Course,HomeWork
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.utils import ValidationError
>>>>>>> 72d4dcbaabb1fd15837327eb8d0b5512a8cc8034


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
<<<<<<< HEAD
class StudentForm(forms.ModelForm):
    GENDER = (
        ("Male", "Male"),
        ("Female", "Female"),
        ("Uknown", "Uknown"),
    )
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    dob = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    gender = forms.CharField(max_length=7, widget=forms.Select(choices=GENDER))
    address = forms.CharField(max_length=200)
    phone = forms.CharField(max_length=15)
    email = forms.EmailField(required = False)
    Organization = forms.CharField(max_length=200)

    class Meta:
        model = lecturer
        fields = ['first_name', 'last_name', 'dob', 'gender', 'address', 'phone', 'email', 'Organization']
=======

class EditCourseForm(forms.ModelForm):
    name = forms.CharField(max_length=100)
    starting_time = forms.DateField()
    ending_time = forms.DateField()
    class Meta:
        model = Course
        fields=['name','starting_time','ending_time']
>>>>>>> 72d4dcbaabb1fd15837327eb8d0b5512a8cc8034

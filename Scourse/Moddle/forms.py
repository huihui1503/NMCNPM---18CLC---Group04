from django import forms
from django.core import validators
from .models import lecturer,student,Course,HomeWork
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.utils import ValidationError


class LecturerForm(forms.ModelForm):
    class Meta:
        model = lecturer
        fields = ['user','first_name','last_name','dob','gender','address','phone','email','Organization']

from django import forms
from django.core import validators
from .models import lecturer,Document
from django.forms.widgets import NumberInput
class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter your email again: ')
    text = forms.CharField(widget=forms.Textarea)
from .models import lecturer,student,Course,HomeWork
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.utils import ValidationError

class LecturerForm(forms.ModelForm):
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
        fields=['first_name','last_name','dob','gender','address','phone','email','Organization']
class StudentForm(forms.ModelForm):
    GENDER = (
        ("Male", "Male"),
        ("Female", "Female"),
        ("Uknown", "Uknown"),
    )
    first_name = forms.CharField(max_length=50, required = False)
    last_name = forms.CharField(max_length=50, required = False)
    dob = forms.DateField(widget=NumberInput(attrs={'type': 'date'}), required = False)
    gender = forms.CharField(max_length=7, widget=forms.Select(choices=GENDER), required = False)
    address = forms.CharField(max_length=200, required = False)
    phone = forms.CharField(max_length=15, required = False)
    email = forms.EmailField(required = False)
    Organization = forms.CharField(max_length=200, required = False)
    class Meta:
        model = student
        fields = ['first_name', 'last_name', 'dob', 'gender', 'address', 'phone', 'email', 'Organization']
class UploadFileForm(forms.Form):
    doc_id = forms.CharField(max_length=15)
    name = forms.CharField(max_length=15)
    lecturer_id = forms.CharField(max_length=15)
    course_id = forms.CharField(max_length = 15)
    doc = forms.FileField()
    class Meta:
        model = Document
        fields = ['doc_id','name','lecturer_id','course_id','address','doc']
class CourseForm(forms.ModelForm):
    name = forms.CharField(max_length=100)
    starting_time = forms.DateField()
    ending_time = forms.DateField()
    class Meta:
        model = Course
        fields=['name','starting_time','ending_time']
        fields=['name','starting_time','ending_time']

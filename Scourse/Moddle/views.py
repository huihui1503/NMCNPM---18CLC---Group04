from django.shortcuts import render
from django.http import HttpResponse
from . import forms
from Moddle.models import Notification,lecturer, student, Course
# Create your views here.

def index(request):
    return render(request, 'index.html')

def redirect_user_type(request):
    return render(request, 'index.html')

def logout(request):
    return render(request, 'logout.html')

def help_page(request):
    my_dict = {'name': 'Group 04', 'email': 'xuanloc2018@gmail.com'}
    return render(request, 'error.html', context=my_dict)

def student(request):
    return render(request, 'student.html')

def teacher(request):
    return render(request, 'lecturer_home.html')

def form_name_view(request):
    form = forms.FormName()
    if request.method == 'POST':
        form = forms.FormName(request.POST)
        if form.is_valid():
            print("VALIDATION SUCCESS!")
            print("NAME: " + form.cleaned_data['name'])
            print("EMAIL: " + form.cleaned_data['email'])
            print("TEXT: " + form.cleaned_data['text'])

    return render(request, 'form_page.html', {'form': form})

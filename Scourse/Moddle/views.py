from django.shortcuts import render
from django.http import HttpResponse
from . import forms
# Create your views here.

def index(request):
    return render(request, 'index.html')
    
def help_page(request):
    my_dict = {'name': 'Group 04', 'email': 'xuanloc2018@gmail.com'}
    return render(request, 'help.html', context=my_dict)

def other(request):
    return render(request, 'other.html')

def relative(request):
    return render(request, 'relative.html')

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

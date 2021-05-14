from django.shortcuts import render
from django.http import HttpResponse
from . import forms
from .forms import LecturerForm
from Moddle.models import Notification,lecturer, student, Course

from .models import Notification,lecturer, student, Course
# Create your views here.

def index(request):
    return render(request, 'index.html')

def redirect_user_type(request):
    if request.user.is_authenticated:
        if request.user.is_student:
            return render(request, 'student.html')
        else:
            return render(request, 'teacher.html')

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
def teacher_info(request,user_id):
    lecturer.objects.get(id = user_id)
    #my_dict ={'user_id': request.user.user_id,'first_name': request.user.first_name,'last_name':request.user.last_name,'dob':request.user.dob,'gender':request.user.gender,'address':request.user.address,'email':request.user.email,'Organization':request.user.Organization}
    return render(request, 'teacher.html')

def teacher_info(request):
    my_dict ={'user_id': '1111','first_name': 'Huy','last_name':'Nguyen Minh','dob':'15/03/2000','gender':'Male','address':'4418 TL10','email':'thaihuy836@gmail.com','Organization':'Hcmus'}
    return render(request, 'teacher_info.html',{})
def teacher_form(request):
    form = LecturerForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {'form': form}
    return render(request, 'teacher_form.html',context)

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

def search(request):
    q=request.GET['q']
    data = Course.objects.filter(name=q).order_by('course_id')
    return render(request,'search.html',{'data':data})

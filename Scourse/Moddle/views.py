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
    return render(request, 'teacher.html')
def teacher_info(request):
    lec = lecturer.objects.get(user = request.user)
    print(request.POST)
    print(lec.last_name)
    init_data ={'user_id':lec.user,'first_name': lec.first_name,'last_name':lec.last_name,'dob':lec.dob,'gender':lec.gender,'address':lec.address,'email':lec.email,'Organization':lec.Organization}
    return render(request, 'teacher_info.html',init_data)


def teacher_form(request):

    lec = lecturer.objects.get(id = request.user)
    form = LecturerForm(request.POST or None,instance = lec)
    if form.is_valid():
        form.save()
    context = {'form': form}
    return render(request, 'teacher_form.html',context)

def student_info(request):
	context = {}
	return render(request, 'student_info.html', context)
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
    data = Course.objects.filter(name=q).order_by('name')
    return render(request,'search.html',{'data':data})

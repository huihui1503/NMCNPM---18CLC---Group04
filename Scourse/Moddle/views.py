from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import forms
<<<<<<< HEAD
from .forms import LecturerForm, StudentForm
=======
from .forms import *
>>>>>>> 72d4dcbaabb1fd15837327eb8d0b5512a8cc8034
from Moddle.models import Notification,lecturer, student, Course

from .models import Notification,lecturer, student, Course
# Create your views here.
from django.views.generic import CreateView, ListView, UpdateView

def index(request):
    return render(request, 'index.html')

def redirect_user_type(request):
    if request.user.is_authenticated:
        if request.user.is_student:
            return render(request, 'student.html')
        else:
            return render(request, 'lecturer_home.html')

    return render(request, 'index.html')

def logout(request):
    return render(request, 'logout.html')

def help_page(request):
    my_dict = {'name': 'Group 04', 'email': 'xuanloc2018@gmail.com'}
    return render(request, 'error.html', context=my_dict)

def Student(request):
    return render(request, 'student.html')

def teacher(request):
    return render(request, 'teacher.html')

def teacher_info(request):
    lec = lecturer.objects.get(user = request.user)
    init_data ={'user_id':lec.user,'first_name': lec.first_name,'last_name':lec.last_name,'dob':lec.dob,'gender':lec.gender,'address':lec.address,'email':lec.email,'Organization':lec.Organization}
    return render(request, 'teacher_info.html',init_data)

<<<<<<< HEAD
=======
def course_info(request):
    _course = Course.objects.get(course_id=request.course_id)
    _courseData = {'course_id': _course.course_id, 'course_name': _course.name, 'startDate': _course.starting_time, 'endDate': _course.ending_time, 'lectureName': _course.lecture_id.first_name + _course.lecture_id.last_name }
    return render(request, "course_info.html", context=_courseData)

def edit_course(request, course_id):
    _course = Course.objects.get(course_id = request.course_id)
    if request.method != 'POST':
        form =  EditCourseForm(instance=_course)
    else:
        form =  EditCourseForm(instance=_course, data=request.POST)
        if form.is_valid():
            form.save()
        context = {'form': form}
    return render(request, 'editcourse_form.html', context)

>>>>>>> 72d4dcbaabb1fd15837327eb8d0b5512a8cc8034
def teacher_form(request):
    lec = lecturer.objects.get(user = request.user)
    form = LecturerForm(request.POST or None,instance = lec)
    if form.is_valid():
        form.save()
    context = {'form': form}
    return render(request, 'teacher_form.html', context)


def student_info(request):
<<<<<<< HEAD
    stu = student.objects.get(user=request.user)
    init_data ={'user_id':stu.user,'first_name': stu.first_name,'last_name':stu.last_name,
                'dob':stu.dob,'gender':stu.gender,'address':stu.address,
                'email':stu.email,'Organization':stu.Organization}
    return render(request, 'student_info.html', init_data)

def student_form(request):
    stu = student.objects.get(user = request.user)
    form = StudentForm(request.POST or None,instance = stu)
    if form.is_valid():
        form.save()
        return redirect("Moddle:student_info")
    context = {'form': form}
    return render(request, 'student_form.html',context)
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
=======
	context = {}
	return render(request, 'student_info.html', context)
>>>>>>> 72d4dcbaabb1fd15837327eb8d0b5512a8cc8034

def search(request):
    q=request.GET['q']
    data = Course.objects.filter(name=q).order_by('name')
    return render(request,'search.html',{'data':data})

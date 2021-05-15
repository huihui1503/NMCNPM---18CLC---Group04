from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import forms
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from .forms import LecturerForm, StudentForm,UploadFileForm
from .forms import *
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
            return render(request, 'teacher.html')

    return render(request, 'index.html')

def logout(request):
    return render(request, 'logout.html')

def help_page(request):
    my_dict = {'name': 'Group 04', 'email': 'xuanloc2018@gmail.com'}
    return render(request, 'error.html', context=my_dict)


def Student(request):
    return render(request, 'student.html')


def course_home(request):
    lec = lecturer.objects.get(user = request.user)
    _courses = Course.objects.filter(lecture_id=lec).order_by('date_added')
    data = {'courses':_courses}
    return render(request, 'course_home.html', context=data)

def register_course(request):
    _courses = Course.objects.all().order_by('date_added')
    data = {'courses':_courses}
    return render(request, 'register_course.html', context=data)

def teacher(request):
    return render(request, 'lecturer_home.html')

def teacher_info(request):
    lec = lecturer.objects.get(user = request.user)
    init_data ={'user_id':lec.user,'first_name': lec.first_name,'last_name':lec.last_name,'dob':lec.dob,'gender':lec.gender,'address':lec.address,'email':lec.email,'Organization':lec.Organization}
    return render(request, 'teacher_info.html',init_data)

def course_info(request, course_id):
    _course = Course.objects.get(course_id = course_id)
    _courseData = {'course_id': _course.course_id, 'course_name': _course.name, 'startDate': _course.starting_time, 'endDate': _course.ending_time, 'lectureName': _course.lecture_id.first_name + _course.lecture_id.last_name }
    return render(request, "course_info.html", context=_courseData)

def edit_course(request, course_id):
    _course = Course.objects.get(course_id = course_id)
    if request.method != 'POST':
        form =  CourseForm(instance=_course)
    else:
        form =  CourseForm(instance=_course, data=request.POST)
        if form.is_valid():
            form.save()
            redirect('course_info.html')

    data= {'form': form, 'course_id': course_id}
    return render(request, 'editcourse_form.html', context=data)

def new_course(request):
    if request.method != 'POST':
        form =  CourseForm()
    else:
        lec = lecturer.objects.get(user = request.user)
        form = CourseForm(data=request.POST)
        if form.is_valid():
            new_course = form.save(commit=False)
            new_course.lecture_id = lec
            form.save()
            return redirect('Moddle:course_home')
    context = {'form': form}
    return render(request, 'new_course.html', context)

def teacher_form(request):
    lec = lecturer.objects.get(user = request.user)
    form = LecturerForm(request.POST or None,instance = lec)
    if form.is_valid():
        form.save()
        return redirect('Moddle:teacher_info')
    context = {'form': form}
    return render(request, 'teacher_form.html', context)

def student_info(request):
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
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            instance = ModelWithFileField(file_field=request.FILES['file'])
            instance.save()
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect_user_type(request)
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {'form': form})
#def form_name_view(request):
    #form = forms.FormName()
    #if request.method == 'POST':
        #form = forms.FormName(request.POST)
        #if form.is_valid():
            #print("VALIDATION SUCCESS!")
            #print("NAME: " + form.cleaned_data['name'])
            #print("EMAIL: " + form.cleaned_data['email'])
            #print("TEXT: " + form.cleaned_data['text'])

    #return render(request, 'form_page.html', {'form': form})
	#context = {}
	#return render(request, 'student_info.html', context)

def search(request):
    q=request.GET['q']
    data = Course.objects.filter(name=q).order_by('name')
    return render(request,'search.html',{'data':data})

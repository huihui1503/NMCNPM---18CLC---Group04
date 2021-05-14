from django.urls import path, include
from . import views

app_name = 'users'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),

    path('register_view/', views.register_view, name='register_view'),
    path(r'^register_student/$', views.register_student_form, name='register_student_form'),
    path(r'^register_teacher/$', views.register_teacher_form, name='register_teacher_form'),
    path('register/', views.register, name='register'),
    path('info/', views.info, name='info'),
    path('exit/', views.exit, name='exit'),
]

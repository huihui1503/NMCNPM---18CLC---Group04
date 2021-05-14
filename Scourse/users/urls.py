from django.urls import path, include
from . import views
from Moddle.views import search
app_name = 'users'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),

    path('register_view/', views.register_view, name='register_view'),
    path(r'^register_student/$', views.register_student_form, name='register_student_form'),
    path(r'^register_teacher/$', views.register_teacher_form, name='register_teacher_form'),
    path('info/search',search,name = "search" ),
    path('exit/', views.exit, name='exit'),
]

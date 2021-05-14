from .views import search
from django.conf.urls import url
from Moddle import views
from django.urls import path

# TEMPLATE TAGGING
app_name = 'Moddle'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^redirect_user_type/$',views.redirect_user_type, name='redirect_user_type'),
    url(r'^teacher/$',views.teacher, name='teacher'),
    url(r'^logout/$',views.logout, name='logout'),
    url(r'^student/$',views.Student, name='student'),

    url(r'^teacher/help_page$',views.help_page, name='help_page'),
    url(r'^teacher/course_home/$',views.course_home, name='course_home'),

    path('teacher/course_home/course_info/<int:course_id>', views.course_info, name='course_info'),
    path('teacher/course_home/course_info/<int:course_id>/edit_course', views.edit_course, name='edit_course'),
    url(r'^teacher/course_home/new_course/$',views.new_course, name='new_course'),
    url(r'^teacher/info/$',views.teacher_info, name='teacher_info'),
    url(r'^teacher/info/form/$',views.teacher_form, name='teacher_form'),
    url(r'^student/info/$', views.student_info, name='student_info'),
    url(r'^student/info/form$',views.student_form, name='student_form'),
    url(r'^search',views.search,name='search'),
    url(r'^redirect_user_type/search',views.search),
    url(r'^student/info/search',views.search),
]

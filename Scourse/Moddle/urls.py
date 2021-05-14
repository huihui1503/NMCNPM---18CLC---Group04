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
    url(r'^student/$',views.student, name='student'),
    url(r'^teacher/help_page$',views.help_page, name='help_page'),
    url(r'^teacher/info/$',views.teacher_info, name='teacher_info'),
    url(r'^teacher/info/form/$',views.teacher_form, name='teacher_form'),
    url(r'^student/info/$', views.student_info, name='student_info'),
    url(r'^search',views.search,name='search'),
    url(r'^redirect_user_type/search',views.search),
    url(r'^student/info/search',views.search),
]

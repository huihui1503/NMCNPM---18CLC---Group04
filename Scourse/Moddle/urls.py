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
<<<<<<< HEAD
    url(r'^teacher/info/form$',views.teacher_form, name='teacher_form'),
=======
    url(r'^search',views.search,name='search')
>>>>>>> 6f8af9d89d733a7306d7ed3bec5af04b93e9dcce
]

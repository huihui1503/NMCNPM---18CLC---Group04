from django.conf.urls import url
from Moddle import views

# TEMPLATE TAGGING
app_name = 'Moddle'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^relative/$',views.relative, name='relative'),
    url(r'^other/$',views.other, name='other'),
]

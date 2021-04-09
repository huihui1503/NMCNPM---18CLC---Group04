from django.conf.urls import url
from Moddle import views

urlpatterns = [
    url(r'^$',views.index, name='index'),
]

# _*_ coding:utf-8 _*_
__author__ = 'PieLs'

from django.conf.urls import url
from django.contrib.auth.views import login

from users import views

urlpatterns = [
    url(r'^login/$', login, {'template_name': 'users/login.html'},
        name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^register/$', views.register, name='register'),
]
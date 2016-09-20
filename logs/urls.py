# coding:utf-8
__author__ = 'PieLs'

from django.conf.urls import url
from logs import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^topics/$', views.topics, name='topics'),
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    url(r'^new_topic/$', views.new_topic, name='new_topic'),
    url(r'new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
    # 用于编辑条目的页面
]
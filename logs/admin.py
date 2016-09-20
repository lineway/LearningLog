# coding:utf-8
from django.contrib import admin
from logs.models import Topic, Entry

# Register your models here.

admin.site.register(Topic)
admin.site.register(Entry)



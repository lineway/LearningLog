# _*_ coding:utf-8 _*_
__author__ = 'PieLs'

from django import forms
from logs.models import Topic, Entry


class TopicForm(forms.ModelForm):

    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}


class EntryForm(forms.ModelForm):

    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
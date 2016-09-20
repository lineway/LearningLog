# coding:utf-8
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from logs.models import Topic
from logs.forms import TopicForm, EntryForm
# Create your views here.

def index(request):
    return render(request, 'logs/index.html')

def topics(request):
    '''
    显示所有的主题
    '''
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'logs/topics.html', context)

def topic(request, topic_id):
    '''
    显示单个主题以及其所有的条目
    '''
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {
        'topic': topic,
        'entries': entries
    }
    return render(request, 'logs/topic.html', context)

def new_topic(request):
    '''
    添加新主题
    '''
    if request.method != 'POST':
        form = TopicForm()
    else:
        # POST提交的数据
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('logs:topics'))

    context = {"form": form}
    return render(request, 'logs/new_topic.html', context)

def new_entry(request, topic_id):
    '''
    在特定的主题下添加新条目
    '''
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('logs:topic', args=[topic_id]))

    context = {'topic': topic, 'form': form}
    return render(request, 'logs/new_topic.html', context)

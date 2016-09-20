# coding:utf-8
from django.db import models

# Create your models here.

class Topic(models.Model):
    '''
    用户学习的主题
    '''
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = u'主题'

    def __unicode__(self):
        '''
        返回模型的字符串表示
        '''
        return self.text

class Entry(models.Model):
    '''
    学到的有关某个主题的具体知识
    '''
    topic = models.ForeignKey(Topic)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = u'详情'

    def __unicode__(self):
        return self.text[:50] + "..."


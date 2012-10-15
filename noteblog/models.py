#!/usr/bin/env python
#-*- coding: utf-8 -*-
from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

class Replay(models.Model):
    name = models.CharField(max_length=20)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(u"分类",max_length = 50)
    
    def __unicode__(self):
        return self.name

class Noteblog(models.Model):
    title = models.CharField(max_length=20)
    context = models.CharField(max_length=50)
    replays = models.ManyToManyField(Replay)
    category = models.ForeignKey(Category)
    user = models.ForeignKey(User)

class NoteblogAdmin(admin.ModelAdmin):
    list_display = ['title','context','user','category']
    search_fields = ['title','context']
    list_filter = ['category']

class Registration(models.Model):
    TYPE_CHOICES=(('M','MAN'),('F','FEMALE'),)
    name = models.CharField(u'用户名',max_length=20)
    password = models.CharField(u'输入密码',max_length=6)
    email = models.EmailField(u'邮箱地址')
    sex = models.CharField(u"性别",max_length=1, choices=TYPE_CHOICES)
    info = models.TextField(u"简介")

class RegistrationAdmin(admin.ModelAdmin):
    list_display = ['name','password','email','sex','info']
    list_filter = ['name','sex']
    search_field = ['name','info']

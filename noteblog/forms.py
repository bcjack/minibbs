#!/usr/bin/env python
#-*- coding: utf-8 -*-
import re
from django import forms
from django.contrib.auth.models import User
from noteblog.models import Registration

class RegistrationForm(forms.ModelForm):
    TYPE_CHOICES=(('M','MAN'),('F','FEMALE'),)
    repassword = forms.CharField(label='重复密码', widget=forms.PasswordInput())
    
    class Meta:
        model = Registration
        widgets = {'password':forms.PasswordInput()}
        #password = forms.CharField(widget=forms.PasswordInput())
        fields = ('name','password','repassword','email','sex','info')

    def clean_name(self):
        name = self.cleaned_data['name']
        if not re.search(r'^\w+$',name):
            raise forms.ValidationError('用户名应该为数字、字母和下划线组成.')
        try:
            User.objects.get(name=name)
        except:
            return name
        raise forms.ValidationError('用户名已经存在')
  
    def clean_repassword(self):
        password = self.cleaned_data['password']
        repassword = self.cleaned_data['repassword']
        if password == repassword:
            return password
        else:
            raise forms.ValidationError('输入不一致')


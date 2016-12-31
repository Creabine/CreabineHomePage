#coding:utf-8
from __future__ import unicode_literals
from django.shortcuts import render
from .forms import ContactUsForm
from .email import send_email

# Create your views here.

def index(request):
    #访问网址时默认弹出首页
    a = request.session
    if request.path == '/':
        return render(request, 'index.html')
    #在网站内跳转至首页
    else:
        return render(request, 'index.html')



def Sports(request):
    return render(request, 'Sports.html')

def Music(request):
    return render(request, 'Music.html')

def Contac(request):
    # 提交表单时发送邮件
    if request.method == 'POST':
        print('request is POST!')
        form = ContactUsForm(request.POST)
        if form.is_valid():
            print('校验通过！')
            cleaned_data = form.cleaned_data
            send_email(request,cleaned_data)
        else:
            #后端校验未通过的时候应该返回提示
            pass
    #跳转页面，提交成功后跳转到首页
    return render(request, 'Contact.html')

def Resume(request):
    return render(request, 'Resume.html')
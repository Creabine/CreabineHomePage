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
        #取得用户的本地语言,判断并决定显示   中文/英文   页面
        #HTTP_ACCEPT_LANGUAGE = request.environ.get('HTTP_ACCEPT_LANGUAGE')
        userLanguage = request.environ.get('HTTP_ACCEPT_LANGUAGE').split(',', 1)[0]
        if userLanguage == 'zh-CN' or userLanguage == 'zh':
            print('中文！')
            config['language'] = 'Chinese'
            return render(request, 'index.html')
        else:
            config['language'] = 'English'
            return render(request, 'index_en.html')
    #在网站内跳转至首页
    else:
        templateName = getTemplateByLanguage(request)
        return render(request,templateName)



def AboutUs(request):
    templateName = getTemplateByLanguage(request)
    return render(request,templateName)

def Inspection(request):
    templateName = getTemplateByLanguage(request)
    return render(request,templateName)

def Test(request):
    templateName = getTemplateByLanguage(request)
    return render(request,templateName)

def Assessment(request):
    templateName = getTemplateByLanguage(request)
    return render(request,templateName)

config = {
    'language':'Chinese',    #默认中文
    'thisTemplateName':'index'   #默认当前页是首页
}




def ContactUs(request):
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
    #跳转页面
    templateName = getTemplateByLanguage(request)
    return render(request, templateName)


#根据语言取得要跳转到的模板
def getTemplateByLanguage(request):
    nextTemplateName =  request.path[1:-5]
    config['thisTemplateName'] = nextTemplateName
    if config['language'] == 'Chinese':
        return request.path[1:-5] + '.html'
    else:
        return request.path[1:-5] + '_en.html'

#改变语言，并跳转至当前页
def ChangeLanguage(request):
    if config['language'] == 'Chinese':
        config['language'] = 'English'
        templateName = config['thisTemplateName'] + '_en.html'
    else:
        config['language'] = 'Chinese'
        templateName = config['thisTemplateName'] + '.html'
    return render(request, templateName)
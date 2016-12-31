#coding:utf-8
from django.core.mail import EmailMultiAlternatives
from .models import ContactMessage
import httplib2, urllib
import time


# 邮件参数
FROM_EMAIL = 'charleschen@xmdaren.com'     #发件箱地址
TO_EMAIL_LIST=['80746965@qq.com']           #收件人(列表)
EMAIL_SUBJECT = '用户联系大仁'               #邮件名称
MAX_RE_SEND_COUNT = 5                         #最大重发次数

def send_email(request,cleaned_data):
    # 通过用户ip获取用户地址：
    userIp = request.environ.get('REMOTE_ADDR')
    #userIp = '110.84.57.236'
    userAddr = get_addr_by_ip(userIp)
    cleaned_data['userAddr'] = userAddr
    # 线判断data的数据类型，然后取得用户填写的各项信息用于构成邮件
    # 邮件内容详细编辑,支持纯文本和html版本，用户不支持html时，使用纯文本。
    textContent = '来自大仁官网的留言\n\n' + '姓名：' + cleaned_data['name'] + '\n' + '公司：' + \
                  cleaned_data['companyName'] + '\n' + '联系电话：' + cleaned_data['telephone'] + \
                  '\n' + '邮箱：' + cleaned_data['email'] + '\n' + '留言内容：' + cleaned_data['message']

    htmlContent = '<p><strong>来自大仁官网的留言</strong><p>' + '<p>姓名：' + cleaned_data['name'] + \
                  '</p>' + '<p>公司：' + cleaned_data['companyName'] + '</p>' + '<p>联系电话：' + \
                  cleaned_data['telephone'] + '</p>' + '<p>邮箱：' + cleaned_data['email'] + '</p>' + \
                  '<p><b>留言内容：' + cleaned_data['message'] + '</b></p>'
    content = EmailMultiAlternatives(EMAIL_SUBJECT, textContent, FROM_EMAIL, TO_EMAIL_LIST)
    content.attach_alternative(htmlContent, 'text/html')
    try:
        content.send()
        # 发送成功后标记：
        cleaned_data['sendCount'] = 1  # 发送了1次
        cleaned_data['sendSucceed'] = 1  # 发送成功
        print('email send Successed!')
    except:
        # 发送失败后标记：
        cleaned_data['sendCount'] = 1  # 发送了1次
        cleaned_data['sendSucceed'] = 0  # 发送失败
        print('email send Falid!')
    # 不论发送成功或失败，都把记录存入数据库
    ContactMessage.objects.create(**cleaned_data)

def get_addr_by_ip(ip):
    params = urllib.parse.urlencode({'ip': ip, 'datatype': 'jsonp', 'callback': 'find'})
    url = 'http://api.ip138.com/query/?' + params
    headers = {"token": "eaba69120d2e556152b1c6b2d7779d3f"}
    http = httplib2.Http()
    response, content = http.request(url, 'GET', headers=headers)
    content = content.decode().split('"')
    addr = content[7] + ';' + content[11] + '.' + content[13] + '.' + content[15]
    return addr

# 下边的函数暂时没用到
# 功能是当有邮件发送失败的时候，重发并记录。
# 但是目前没实现循环的部分

def re_send_email():
    # 若没有发送失败的邮件，则结束，否则发送
    if not ContactMessage.objects.filter(sendSucceed=0).exclude(sendCount=MAX_RE_SEND_COUNT).exists():
        print('no email need to sent!')
        return
    else:
        # 有邮件时取第一个构成邮件并尝试发送
        emailData = ContactMessage.objects.filter(sendSucceed=0).exclude(sendCount=MAX_RE_SEND_COUNT).order_by('created')[0]
        textContent = '来自大仁官网的留言\n\n' + '姓名：' + emailData.name + '\n' + '公司：' + \
                      emailData.companyName + '\n' + '联系电话：' + emailData.telephone + \
                      '\n' + '邮箱：' + emailData.email + '\n' + '留言内容：' + emailData.message
        htmlContent = '<p><strong>来自大仁官网的留言</strong><p>' + '<p>姓名：' + emailData.name + \
                      '</p>' + '<p>公司：' + emailData.companyName + '</p>' + '<p>联系电话：' + \
                      emailData.telephone + '</p>' + '<p>邮箱：' + emailData.email + '</p>' + \
                      '<p><b>留言内容：' + emailData.message + '</b></p>'
        content = EmailMultiAlternatives(EMAIL_SUBJECT, textContent, FROM_EMAIL, TO_EMAIL_LIST)
        content.attach_alternative(htmlContent, 'text/html')
        try:
            content.send()
            # 发送成功后更新数据库
            newCount = emailData.sendCount + 1
            ContactMessage.objects.filter(id=emailData.id).update(sendCount=newCount,sendSucceed=1)
            print('email re-send Successed!')
        except:
            # 发送失败后更新数据库
            newCount = emailData.sendCount + 1
            ContactMessage.objects.filter(id=emailData.id).update(sendCount=newCount, sendSucceed=1)
            print('email re-send Falid!')
        # 不论发送成功或失败，都更新发送记录，存入数据库
    print('ok')


def re_exe(func, inc=120):
    while True:
        func()
        time.sleep(inc)






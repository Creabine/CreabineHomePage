from django import forms

class ContactUsForm(forms.Form):
    name = forms.CharField(label='联系人名称', max_length=16, error_messages={
        'required': '请填写您的称呼',
        'max_length': '称呼太长'
    })

    email = forms.EmailField(label='联系人邮箱', error_messages={
        'required': '请填写您的邮箱',
        'invalid': '邮箱格式不正确'
    })

    message = forms.CharField(label='留言', error_messages={
        'required': '请填写您的评论内容',
        'max_length': '评论内容太长'
    })


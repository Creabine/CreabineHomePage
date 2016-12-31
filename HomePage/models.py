from django.db import models

# Create your models here.
class ContactMessage(models.Model):
    #称呼
    name = models.CharField('联系人名称', max_length=16)
    # 公司名称
    companyName = models.CharField('公司名称', max_length=32)
    # 联系电话
    telephone = models.CharField('联系人电话', max_length=16)
    # 联系邮箱
    email = models.EmailField('联系人邮箱')
    # 留下的信息
    message = models.TextField('留言')
    #发布时间
    created = models.DateTimeField('发布时间', auto_now_add=True)
    # 发送次数
    sendCount = models.IntegerField('邮件发送次数')
    # 发送成功标记
    sendSucceed = models.IntegerField('邮件发送成功')
    # 用户ip及地址
    userAddr = models.CharField('用户ip及地址', max_length=32)

    # 用于admin中显示
    def __str__(self):
        return self.companyName

    def get_send_result(self):
        if self.sendSucceed == 1:
            return u'<span style="color:green;font-weight:bold">%s</span>' % (u"成功",)
        else:
            return u'<span style="color:red;font-weight:bold">%s</span>' % (u"失败",)
    get_send_result.short_description = '邮件发送状态'
    get_send_result.allow_tags = True
    #sendSucceedStr = property(get_send_result)

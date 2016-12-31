from django.contrib import admin
from HomePage.models import ContactMessage
# Register your models here.
# 自定义过滤器
class emailSendResultFilter(admin.SimpleListFilter):
    title = (u'邮件发送状态')
    parameter_name = 'sendSucceed'

    def lookups(self, request, model_admin):
        return (
            (1,u'成功'),
            (0,u'失败')

        )
    def queryset(self, request, queryset):
        if self.value():
            if int(self.value()) == 0:
                return queryset.filter(sendSucceed=0)
            if int(self.value()) == 1:
                return queryset.filter(sendSucceed=1)

#admin配置
class ContactMessageAdmin(admin.ModelAdmin):
    # 每个列表中的显示项
    list_display = ('name','email','get_send_result')
    # 搜索框，参数是搜索域
    search_fields = ('name','email','message')
    # 过滤器，参数是自定义过滤器
    list_filter = (emailSendResultFilter,)

# 注册要显示的表
admin.site.register(ContactMessage,ContactMessageAdmin)
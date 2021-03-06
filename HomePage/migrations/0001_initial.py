# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-31 07:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, verbose_name='联系人名称')),
                ('companyName', models.CharField(max_length=32, verbose_name='公司名称')),
                ('telephone', models.CharField(max_length=16, verbose_name='联系人电话')),
                ('email', models.EmailField(max_length=254, verbose_name='联系人邮箱')),
                ('message', models.TextField(verbose_name='留言')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='发布时间')),
                ('sendCount', models.IntegerField(verbose_name='邮件发送次数')),
                ('sendSucceed', models.IntegerField(verbose_name='邮件发送成功')),
                ('userAddr', models.CharField(max_length=32, verbose_name='用户ip及地址')),
            ],
        ),
    ]

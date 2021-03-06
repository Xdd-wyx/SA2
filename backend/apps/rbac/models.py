from django.db import models
from django.contrib.auth.models import AbstractUser, Group
from datetime import datetime
import time

# Create your models here.


class UserAuth(models.Model):
    """登录日志"""
    username = models.CharField(max_length=200, verbose_name="账号", help_text='账号')
    remote_addr = models.CharField(max_length=50, default='', verbose_name="客户端地址", help_text='客户端地址')
    status = models.CharField(max_length=20, verbose_name='认证状态', help_text='认证状态')
    remote_agent = models.TextField(default='', verbose_name="客户端信息", help_text='客户端信息')
    token = models.TextField(default='', verbose_name='Token', help_text='Token')
    add_time = models.DateTimeField(auto_now_add=True, help_text='登录时间', verbose_name="登录时间")
    update_time = models.DateTimeField(auto_now=True, help_text='更新时间', verbose_name='更新时间')

    class Meta:
        verbose_name = "登录日志"
        verbose_name_plural = verbose_name
        ordering = ['id']


class GroupProfile(Group):
    add_time = models.DateTimeField(default=datetime.now, verbose_name="创建时间")
    update_time = models.DateTimeField('更新时间', auto_now=True, help_text='更新时间')

    class Meta:
        verbose_name = '用户组'
        verbose_name_plural = verbose_name

    @property
    def permissions2(self):
        return self.permissions.all().values()


class UserProfile(AbstractUser):
    """用户"""
    name = models.CharField(max_length=20, default="", verbose_name="姓名")
    mobile = models.CharField(max_length=11, default="", verbose_name="手机号码")
    avatar = models.ImageField(upload_to="static/%Y/%m", default="image/default.png",
                              max_length=100, null=True, blank=True)
    position = models.CharField(max_length=50, null=True, blank=True, verbose_name="职位")

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name
        ordering = ['id']

    @property
    def roles(self):
        roles = GroupProfile.objects.filter(user=self).values('name')
        return [x.get('name') for x in roles if roles]

    @property
    def permissions(self):
        groups_permissions = GroupProfile.objects.filter(user=self)
        print([x.permissions.all() for x in groups_permissions])
        return 1111

    def __str__(self):
        return self.username


class IpWhiteList(models.Model):
    """ip白名单"""
    ip_addr = models.GenericIPAddressField(verbose_name="白名单")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    update_time = models.DateTimeField(auto_now=True, help_text='更新时间', verbose_name='更新时间')

    class Meta:
        verbose_name = '权限白名单'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.ip_addr



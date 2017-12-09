# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


from datetime import datetime


class Theme(models.Model):
    image = models.ImageField(upload_to="zhuti/%Y/%m", verbose_name=u"主题", max_length=300)
    add_time = models.DateField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"主题"
        verbose_name_plural = verbose_name


class Contact(models.Model):
    content1 = models.CharField(max_length=30, verbose_name=u"心全Health Box招商热线")
    content2 = models.CharField(max_length=30, verbose_name=u"产品服务热线")
    content3 = models.CharField(max_length=100, verbose_name=u"企业地址")
    image = models.ImageField(upload_to="erweima/%Y/%m", verbose_name=u"二维码", max_length=100)
    add_time = models.DateField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"联系我们"
        verbose_name_plural = verbose_name
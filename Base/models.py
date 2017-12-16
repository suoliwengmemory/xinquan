# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


from datetime import datetime


class Bow(models.Model):
    title = models.CharField(max_length=50, verbose_name=u"导航修改")
    bar1 = models.CharField(max_length=50, verbose_name=u"导航栏一")
    bar2 = models.CharField(max_length=50, verbose_name=u"导航栏二")
    bar3 = models.CharField(max_length=50, verbose_name=u"导航栏三")
    bar4 = models.CharField(max_length=50, verbose_name=u"导航栏四")
    bar5 = models.CharField(max_length=50, verbose_name=u"导航栏五")
    bar6 = models.CharField(max_length=50, verbose_name=u"导航栏六")
    bar7 = models.CharField(max_length=50, verbose_name=u"导航栏七")
    image = models.ImageField(upload_to="tabbar/%Y/%m", verbose_name=u"LOGO", max_length=50)
    Telephone = models.CharField(max_length=30, verbose_name=u"联系电话")
    add_time = models.DateField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"首部导航栏"
        verbose_name_plural = verbose_name

class Side(models.Model):
    title = models.CharField(max_length=50, verbose_name=u"导航修改")
    bar = models.CharField(max_length=50, verbose_name=u"首页导航")
    bar1 = models.CharField(max_length=50, verbose_name=u"导航栏一")
    bar2 = models.CharField(max_length=50, verbose_name=u"导航栏二")
    bar3 = models.CharField(max_length=50, verbose_name=u"导航栏三")
    bar4 = models.CharField(max_length=50, verbose_name=u"导航栏四")
    bar5 = models.CharField(max_length=50, verbose_name=u"导航栏五")
    bar6 = models.CharField(max_length=50, verbose_name=u"导航栏六")
    bar7 = models.CharField(max_length=50, verbose_name=u"导航栏七")
    Telephone = models.CharField(max_length=30, verbose_name=u"联系电话")
    add_time = models.DateField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"左部导航栏"
        verbose_name_plural = verbose_name


class Tabbar(models.Model):
    title = models.CharField(max_length=50, verbose_name=u"导航修改")
    bar1 = models.CharField(max_length=50, verbose_name=u"导航栏一")
    bar2 = models.CharField(max_length=50, verbose_name=u"导航栏二")
    bar3 = models.CharField(max_length=50, verbose_name=u"导航栏三")
    bar4 = models.CharField(max_length=50, verbose_name=u"导航栏四")
    bar5 = models.CharField(max_length=50, verbose_name=u"导航栏五")
    bar6 = models.CharField(max_length=50, verbose_name=u"导航栏六")
    bar7 = models.CharField(max_length=50, verbose_name=u"导航栏七")
    image = models.ImageField(upload_to="tabbar/%Y/%m", verbose_name=u"二维码", max_length=100)
    record = models.CharField(max_length=200, verbose_name=u"备案栏")
    Telephone = models.CharField(max_length=30, verbose_name=u"联系电话")
    add_time = models.DateField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"底部导航栏"
        verbose_name_plural = verbose_name


# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals
from DjangoUeditor.models import UEditorField


from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.six import python_2_unicode_compatible

from datetime import datetime


class Theme(models.Model):
    title = models.CharField(max_length=30, verbose_name=u"标题", default="")
    detail = UEditorField(verbose_name="左侧标签", width=600, height=200, imagePath="zhuti/ueditor/",
                          filePath="zhuti/ueditor/", default="")
    title2 = models.CharField(max_length=30, verbose_name=u"正文标签", default="")
    image = models.ImageField(upload_to="zhuti/%Y/%m", verbose_name=u"主题", blank=True, max_length=300)
    add_time = models.DateField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"主题"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.title


class Store(models.Model):
    title = models.CharField(max_length=30, verbose_name=u"标题")
    show = models.CharField(choices=(("yes", "显示"), ("qx", "不显示")), max_length=3, verbose_name="首页显示", default="")
    image = models.ImageField(upload_to="fengmian/%Y/%m", verbose_name=u"封面", blank=True, max_length=100)
    image1 = models.ImageField(upload_to="dianpu/%Y/%m", verbose_name=u"轮播图1", blank=True, max_length=100)
    image2 = models.ImageField(upload_to="dianpu/%Y/%m", verbose_name=u"轮播图2", blank=True, max_length=100)
    image3 = models.ImageField(upload_to="dianpu/%Y/%m", verbose_name=u"轮播图3", blank=True, max_length=100)
    image4 = models.ImageField(upload_to="dianpu/%Y/%m", verbose_name=u"轮播图4", blank=True, max_length=100)
    image5 = models.ImageField(upload_to="dianpu/%Y/%m", verbose_name=u"轮播图5", blank=True, max_length=100)
    detail = UEditorField(verbose_name="店铺内容", width=600, height=600,  imagePath="dianpu/ueditor/", filePath="dianpu/ueditor/", default="")
    add_time = models.DateField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"店铺"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
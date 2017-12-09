# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals
from DjangoUeditor.models import UEditorField

from django.db import models
from datetime import datetime


class Theme(models.Model):
    image = models.ImageField(upload_to="zhuti/%Y/%m", verbose_name=u"主题", max_length=300)
    add_time = models.DateField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"主题"
        verbose_name_plural = verbose_name


class Kind(models.Model):
    kind = models.CharField(max_length=100, verbose_name=u"产品种类", default="")
    add_time = models.DateField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"产品种类"
        verbose_name_plural = verbose_name


class Product(models.Model):
    type = models.CharField(max_length=10, verbose_name=u"类别", default="")
    title = models.CharField(max_length=30, verbose_name=u"标题", default="")
    show = models.CharField(choices=(("yes", "显示"), ("qx", "不显示")), max_length=3, verbose_name="首页显示", default="")
    image = models.ImageField(upload_to="chanpin/%Y/%m", verbose_name=u"封面", max_length=100, default="")
    detail = UEditorField(verbose_name="产品简介", width=600, height=600,  imagePath="chanpin/ueditor/", filePath="chanpin/ueditor/", default="")
    add_time = models.DateField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"药柜"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


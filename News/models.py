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
    image = models.ImageField(upload_to="zhuti/%Y/%m", blank=True, verbose_name=u"主题", max_length=300)
    add_time = models.DateField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"主题"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.title

@python_2_unicode_compatible
class News(models.Model):
    title = models.CharField(max_length=30, verbose_name=u"标题")
    show = models.CharField(choices=(("yes", "显示"), ("qx", "不显示")), max_length=3, verbose_name="首页显示", default="")
    image = models.ImageField(upload_to="xinwen/%Y/%m", verbose_name=u"封面", blank=True, max_length=100, default="")
    detail1 = UEditorField(verbose_name="概述", width=740, height=200, imagePath="xinwen/ueditor/",filePath="xinwen/ueditor/", default="")
    detail = UEditorField(verbose_name="新闻内容", width=740, height=600,  imagePath="xinwen/ueditor/", filePath="xinwen/ueditor/", default="")
    add_time = models.DateField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"新闻"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('newsdet', kwargs={'pk': self.pk})






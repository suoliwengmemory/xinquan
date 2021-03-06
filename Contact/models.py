# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from DjangoUeditor.models import UEditorField


from datetime import datetime


class Theme(models.Model):
    title = models.CharField(max_length=30, verbose_name=u"标题", default="")
    detail = UEditorField(verbose_name="左侧标签", width=600, height=200, imagePath="zhuti/ueditor/",filePath="zhuti/ueditor/", default="")
    title2 = models.CharField(max_length=30, verbose_name=u"正文标签", default="")
    image = models.ImageField(upload_to="zhuti/%Y/%m", verbose_name=u"主题", blank=True, max_length=300)
    add_time = models.DateField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"主题"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.title

class Contact(models.Model):
    content1 = models.CharField(max_length=30, verbose_name=u"心全Health Box招商热线")
    content2 = models.CharField(max_length=30, verbose_name=u"产品服务热线")
    content3 = models.CharField(max_length=100, verbose_name=u"企业地址")
    image = models.ImageField(upload_to="erweima/%Y/%m", verbose_name=u"二维码", blank=True, max_length=100)
    add_time = models.DateField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"联系我们"
        verbose_name_plural = verbose_name
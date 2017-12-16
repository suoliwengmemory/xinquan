# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals
from DjangoUeditor.models import UEditorField


from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.six import python_2_unicode_compatible

from datetime import datetime


class Index(models.Model):
    title = models.CharField(max_length=100, verbose_name=u"图片名")
    high = models.CharField(max_length=30, verbose_name=u"图片高度")
    image = models.ImageField(upload_to="shouye/%Y/%m", verbose_name=u"封面", blank=True, default="", max_length=100)
    url = models.URLField(verbose_name=u"链接地址", max_length=100, blank=True, default="")
    add_time = models.DateField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"首页"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
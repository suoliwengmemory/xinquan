# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-11 20:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Goods', '0014_auto_20171211_2015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='', upload_to='chanpin/%Y/%m', verbose_name='封面'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image1',
            field=models.ImageField(upload_to='chanpin/%Y/%m', verbose_name='轮播图1'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image2',
            field=models.ImageField(upload_to='chanpin/%Y/%m', verbose_name='轮播图2'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image3',
            field=models.ImageField(upload_to='chanpin/%Y/%m', verbose_name='轮播图3'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image4',
            field=models.ImageField(upload_to='chanpin/%Y/%m', verbose_name='轮播图4'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image5',
            field=models.ImageField(upload_to='chanpin/%Y/%m', verbose_name='轮播图5'),
        ),
    ]

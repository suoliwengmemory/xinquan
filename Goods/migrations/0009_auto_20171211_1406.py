# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-11 14:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Goods', '0008_auto_20171211_1401'),
    ]

    operations = [
        migrations.RenameField(
            model_name='kind',
            old_name='kind',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='type',
            new_name='kind',
        ),
    ]

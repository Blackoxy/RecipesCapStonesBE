# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-11-06 17:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_auto_20181105_2357'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='picture',
            field=models.CharField(default='', max_length=300),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-11-05 23:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=models.CharField(max_length=500),
        ),
    ]

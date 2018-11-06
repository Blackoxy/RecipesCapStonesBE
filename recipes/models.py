# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=40)
    picture = models.CharField(max_length=300)
    description = models.CharField(max_length=500)
    ingredients = models.CharField(max_length=500)

    def __str__(self):
        return self.name
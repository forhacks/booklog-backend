# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=200)


class Category(models.Model):
    title = models.CharField(max_length=200)
    amazon_id = models.CharField(max_length=30)


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.TextField()
    image = models.URLField()
    amazon_id = models.CharField(max_length=30)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)



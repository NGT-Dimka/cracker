# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.db import models

class Post(models.Model): # создаем модель пост
    title = models.CharField(max_length=255) # заголовок поста
    datetime = models.DateTimeField(u'Дата публикации') # дата публикации
    content = models.TextField(max_length=10000) # текст поста

    def __unicode__(self): # функция возвращающая заголовок поста
        return self.title

    def get_absolute_url(self): # функция создает урл равный номеру поста
        return "/blog/%i/" % self.id
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from blog.models import Post
from django.views.generic import ListView, DetailView

class PostsListView(ListView): # модель отображения списка постов
    model = Post

class PostDetailView(DetailView): # модель детального отображения поста
    model = Post
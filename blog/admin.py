from __future__ import unicode_literals # импорт юникода

from django.contrib import admin # импорт библиотеки админа
from blog.models import Post # импорт модели пост из списка моделей блога

admin.site.register(Post) # предоставление прав только единственному пользователю админу
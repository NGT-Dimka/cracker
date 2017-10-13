from django.conf.urls import url

from blog.views import PostsListView, PostDetailView # импортируем варианты отображения

urlpatterns = [
    url(r'^$', PostsListView.as_view(), name='list'), # первое отображение список постов
    url(r'^(?P<pk>\d+)/$', PostDetailView.as_view()), # второе - детальное отображение поста
]
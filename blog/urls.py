from django.contrib import admin
from django.urls import path

from blog.views.post_create_view import PostCreateView
from blog.views.post_list_by_tag_view import PostListByTag

urlpatterns = [
    path('create/', PostCreateView.as_view(), name='post-create'),
    path('post-list/<slug>/', PostListByTag.as_view(), name='post-list-by-tag'),
]

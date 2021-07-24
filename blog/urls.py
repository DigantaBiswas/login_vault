from django.contrib import admin
from django.urls import path

from blog.views.post_create_view import PostCreateView

urlpatterns = [
    path('create/', PostCreateView.as_view(), name='post-create'),
]

from django.contrib import admin
from django.urls import path

from blog.sitemaps.item_site_maps import ItemSitemap
from blog.views.post_create_view import PostCreateView
from blog.views.post_list_by_tag_view import PostListByTag
from django.contrib.sitemaps.views import sitemap

sitemaps = {
    'posts': ItemSitemap
}

urlpatterns = [
    path('create/', PostCreateView.as_view(), name='post-create'),
    path('post-list/<name>/', PostListByTag.as_view(), name='post-list-by-tag'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap')
]

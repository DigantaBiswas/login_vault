from django.shortcuts import render
from django.views import View

from blog.models import Tag, Post


class PostListByTag(View):

    def get(self, request, name):
        """ title is used to show in page html as html title"""
        title = name

        tag = Tag.objects.filter(name=name).last()
        posts = Post.objects.filter(tag__in=[tag])

        context = {
            'posts': posts,
            'title': title
        }
        return render(request, 'blog/post_list.html', context)

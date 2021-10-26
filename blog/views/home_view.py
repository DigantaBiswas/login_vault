from django.db.models import Q
from django.shortcuts import render
from django.views import View

from blog.models import Tag, Post


class HomeView(View):
    def get(self, request):
        tags = Tag.objects.filter().order_by('?')[:50]
        context = {
            'tags': tags,
            'title': "Home"
        }
        return render(request, 'base/login_vault_home.html', context)

    def post(self, request):
        search_text = request.POST.get("search_text")

        posts = Post.objects.filter(Q(title__icontains=search_text) | Q(detail__icontains=search_text))

        context = {
            'posts':posts
        }
        return render(request, 'blog/post_list.html', context)
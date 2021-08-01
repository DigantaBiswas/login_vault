from django.shortcuts import render
from django.views import View

from blog.models import Tag


class HomeView(View):

    def get(self, request):
        tags = Tag.objects.filter()[:50]
        context = {
            'tags': tags,
            'title': "Home"
        }
        return render(request, 'base/login_vault_home.html', context)

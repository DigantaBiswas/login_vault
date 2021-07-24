from django.shortcuts import render
from django.views import View


class PostCreateView(View):
    def get(self, request):
        return render(request, 'blog/post_create.html')

from django.shortcuts import render
from django.views import View


class HomeView(View):

    def get(self, request):
        return render(request, 'base/login_vault_home.html')
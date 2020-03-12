from django.shortcuts import render
from django.views.generic import ListView
from front.user_manager.models import UserManager

class UserManagerView(ListView):
    model = UserManager
    def index(request):
        return render(request, 'user_manager/index.html.haml')
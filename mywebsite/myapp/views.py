from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import myModel
from .models import User

def homepage(request):
    return render(request, 'homepage.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import myModel

def home(request):
    return HttpResponse("Welcome to Zhehao Zhao's dynamic Django website!")

def my_view(request):
    items = myModel.objects.all()
    return render(request, 'my_template.html', {'items': items})


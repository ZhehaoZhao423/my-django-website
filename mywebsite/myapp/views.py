from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import myUser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class HelloWorld(APIView):
    def get(self, request):
        return Response({"message": "Hello, World!"}, status=status.HTTP_200_OK)

def homepage(request):
    return render(request, 'homepage.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def user_list(request):
    users = myUser.objects.all()
    return render(request, 'user_list.html', {'users': users})

def profile_view(request):
    return HttpResponse("You have login successfully. This is the user profile page.")

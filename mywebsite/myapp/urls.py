from django.urls import path
from .views import homepage, user_list, about, contact, HelloWorld, profile_view

urlpatterns = [
    path('', homepage, name='homepage'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('userlist/', user_list, name='user_list'),
    path('hello/', HelloWorld.as_view(), name='hello-world'),
    path('accounts/profile/', profile_view, name='profile'),
]


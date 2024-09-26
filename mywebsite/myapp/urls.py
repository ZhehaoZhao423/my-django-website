from django.urls import path
from .views import homepage, user_list, about, contact

urlpatterns = [
    path('', homepage, name='homepage'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('userlist/', user_list, name='user_list'),
]


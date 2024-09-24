from django.urls import path
from .views import my_view  # 导入你的视图

urlpatterns = [
    path('', my_view, name='my_view'),  # 定义根URL的路由
]


from django.urls import path
from .api import BlogListAPI, BlogDetailAPI

urlpatterns = [
    path('', BlogListAPI.as_view(), name='api_blog_list'),
    path('<int:pk>/', BlogDetailAPI.as_view(), name='api_blog_detail'),
]

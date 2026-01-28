from django.urls import path
from . import views

urlpatterns = [
    path('', views.page, name='forum_home'),     # ← ADD THIS
    path('create/', views.create_post, name='create_post'),
]

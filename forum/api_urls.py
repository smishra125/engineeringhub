from django.urls import path
from .api import ForumListCreateAPI

urlpatterns = [
    path('', ForumListCreateAPI.as_view(), name='api_forum'),
]

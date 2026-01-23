from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import BlogPost
from .serializers import BlogPostSerializer
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

class BlogViewSet(ReadOnlyModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'category']
    ordering_fields = ['created_at']

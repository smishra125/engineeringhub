from rest_framework import generics
from .models import BlogPost
from .serializers import BlogPostSerializer

class BlogListAPI(generics.ListAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

class BlogDetailAPI(generics.RetrieveAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import ForumPost
from .serializers import ForumPostSerializer

class ForumViewSet(ModelViewSet):
    queryset = ForumPost.objects.all().order_by('-created_at')
    serializer_class = ForumPostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'message']
    ordering_fields = ['created_at']

    def perform_create(self, serializer):
        # THIS IS CRITICAL
        serializer.save(user=self.request.user)

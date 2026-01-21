from rest_framework import generics, permissions
from .models import ForumPost
from .serializers import ForumPostSerializer

class ForumListCreateAPI(generics.ListCreateAPIView):
    queryset = ForumPost.objects.all()
    serializer_class = ForumPostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

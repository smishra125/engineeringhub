from rest_framework import serializers
from .models import ForumPost

class ForumPostSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = ForumPost
        fields = ['id', 'user', 'title', 'message', 'created_at']
        read_only_fields = ['user', 'created_at']

from rest_framework import serializers
from .models import ForumPost

class ForumPostSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = ForumPost
        fields = "__all__"

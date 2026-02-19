from django.shortcuts import render
from .models import Video

def video_list(request):
    videos = Video.objects.all().order_by('-created_at')
    return render(request, "videos/list.html", {"videos": videos})

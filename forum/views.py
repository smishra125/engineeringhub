from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import ForumPost

@login_required
def create_post(request):
    if request.method == "POST":
        ForumPost.objects.create(
            user=request.user,
            title=request.POST['title'],
            message=request.POST['message']
        )
        return redirect('/')
    return render(request, "forum/create_post.html")

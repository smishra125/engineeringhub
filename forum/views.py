from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import ForumPost

@login_required
def create_post(request):
    if request.method == "POST":
        ForumPost.objects.create(
            user=request.user,
            title=request.POST.get("title"),
            message=request.POST.get("message")
        )
        return redirect('forum_home')

    return render(request, 'forum/create_post.html')

def page(request):
    posts = ForumPost.objects.order_by('-created_at')
    return render(request, 'forum/page.html', {'posts': posts})
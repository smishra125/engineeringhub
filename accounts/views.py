from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from forum.models import ForumPost
from blog.models import BlogPost


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'accounts/signup.html', {'form': form})

@login_required
def profile(request):
    forum_posts = ForumPost.objects.filter(user=request.user).order_by("-created_at")
    blog_posts = BlogPost.objects.filter(author=request.user).order_by("-created_at")

    return render(request, "accounts/profile.html", {
        "forum_posts": forum_posts,
        "blog_posts": blog_posts,
    })

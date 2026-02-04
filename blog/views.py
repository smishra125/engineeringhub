from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import BlogPost
from django.contrib.auth.models import User
from .forms import BlogForm, CommentForm


@login_required
def blog_edit(request, pk):
    post = get_object_or_404(BlogPost, pk=pk, author=request.user)

    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect("blog_detail", pk=post.pk)
    else:
        form = BlogForm(instance=post)

    return render(request, "blog/edit.html", {"form": form})

@login_required
def blog_delete(request, pk):
    post = get_object_or_404(BlogPost, pk=pk, author=request.user)

    if request.method == "POST":
        post.delete()
        return redirect("blog_list")

    return render(request, "blog/delete.html", {"post": post})

@login_required
def create_blog(request):
    if request.method == "POST":
        title = request.POST.get("title")
        category = request.POST.get("category")
        content = request.POST.get("content")
        image = request.FILES.get("cover_image")

        BlogPost.objects.create(
            title=title,
            category=category,
            content=content,
            cover_image=image,
            author=request.user
        )

        return redirect("blog_list")

    return render(request, "blog/create_blog.html")

def blog_list(request):
    posts = BlogPost.objects.order_by("-created_at")

    if request.user.is_authenticated and request.GET.get("mine"):
        posts = posts.filter(author=request.user)

    return render(request, "blog/page.html", {
        "posts": posts
    })


# def blog_detail(request, pk):
#     post = get_object_or_404(BlogPost, pk=pk)
#     return render(request, "blog/detail.html", {"post": post})

def page(request):
    posts = BlogPost.objects.order_by('-created_at')
    return render(request, 'blog/page.html', {'posts': posts})


def blog_detail(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    comments = post.comments.order_by("-created_at")

    if request.method == "POST" and request.user.is_authenticated:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            return redirect("blog_detail", pk=pk)
    else:
        form = CommentForm()

    return render(request, "blog/detail.html", {
        "post": post,
        "comments": comments,
        "form": form
    })

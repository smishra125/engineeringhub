from django.shortcuts import render
from .models import BlogPost

def page(request):
    posts = BlogPost.objects.order_by('-created_at')
    return render(request, 'blog/page.html', {'posts': posts})

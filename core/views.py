from django.shortcuts import render
from marketplace.models import Product
from blog.models import BlogPost
from scraper.models import ScrapedPost
from forum.models import ForumPost

def home(request):
    products = Product.objects.all()[:4]
    posts = BlogPost.objects.order_by('-created_at')[:4]  # 🔥 change here
    forum_posts = ForumPost.objects.order_by('-created_at')[:3]

    return render(request, 'core/home.html', {
        'products': products,
        'posts': posts,
        'forum_posts': forum_posts,
    })

def about(request):
    return render(request, "core/about.html")

# def home(request):
#     return render(request, 'core/home.html')

# def home(request):
#     products = Product.objects.all()[:4]
#     return render(request, 'core/home.html', {'products': products})

# def home(request):
#     products = Product.objects.all()[:4]
#     posts = BlogPost.objects.order_by('-created_at')[:2]
#     return render(request, 'core/home.html', {
#         'products': products,
#         'posts': posts
#     })


# scraped = ScrapedPost.objects.order_by('-created_at')[:4]

# forum_posts = ForumPost.objects.order_by('-created_at')[:4]

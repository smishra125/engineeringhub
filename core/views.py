from django.shortcuts import render
from marketplace.models import Product
from blog.models import BlogPost
from scraper.models import ScrapedPost
from forum.models import ForumPost



def home(request):
    context = {
        "products": Product.objects.all()[:4],
        "posts": BlogPost.objects.all()[:2],
        "forum_posts": ForumPost.objects.all()[:4],
        "scraped": ScrapedPost.objects.all()[:4],
    }
    return render(request, "core/home.html", context)

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

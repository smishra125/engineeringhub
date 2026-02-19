from django.shortcuts import render
from django.core.paginator import Paginator
from marketplace.models import Product
from blog.models import BlogPost
from scraper.models import ScrapedPost
from forum.models import ForumPost

def home(request):
    products = Product.objects.all()[:4]

    blog_list = BlogPost.objects.order_by('-created_at')
    paginator = Paginator(blog_list, 3)  # show 4 blogs per page

    page_number = request.GET.get('page')
    blogs = paginator.get_page(page_number)

    forum_posts = ForumPost.objects.order_by('-created_at')[:3]

    return render(request, 'core/home.html', {
        'products': products,
        'blogs': blogs,   # 👈 IMPORTANT: use blogs not posts
        'forum_posts': forum_posts,
    })

def about(request):
    return render(request, "core/about.html")

def feature_flags(request):
    return {
        "ENABLE_FORUM": settings.ENABLE_FORUM,
        "ENABLE_AI": settings.ENABLE_AI,
    }

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

from .models import Product
from django.core.paginator import Paginator
from .models import Product
from django.shortcuts import render, get_object_or_404


def product_list(request):
    product_list = Product.objects.all()
    paginator = Paginator(product_list, 8)  # 8 products per page

    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)

    return render(request, "marketplace/product_list.html", {
        "products": products
    })

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, "marketplace/product_detail.html", {
        "product": product
    })

def page(request):
    products = Product.objects.all()
    return render(request, 'marketplace/page.html', {'products': products})
from django.shortcuts import render, get_object_or_404, redirect
from .models import OurProduct, ProductLike, ProductComment
from django.contrib.auth.decorators import login_required
from .forms import ProductCommentForm


def product_list(request):
    products = OurProduct.objects.all().order_by('-created_at')
    return render(request, 'our_products/list.html', {
        'products': products
    })

def product_detail(request, pk):
    product = get_object_or_404(OurProduct, pk=pk)
    comments = product.comments.all().order_by("-created_at")

    is_liked = False
    if request.user.is_authenticated:
        is_liked = product.likes.filter(user=request.user).exists()

    if request.method == "POST":
        if not request.user.is_authenticated:
            return redirect("login")

        form = ProductCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.product = product
            comment.user = request.user
            comment.save()
            return redirect("product_detail", pk=product.id)
    else:
        form = ProductCommentForm()

    return render(request, "our_products/detail.html", {
        "product": product,
        "comments": comments,
        "comment_form": form,
        "is_liked": is_liked, 
    })


@login_required
def product_like(request, pk):
    product = get_object_or_404(OurProduct, pk=pk)

    like, created = ProductLike.objects.get_or_create(
        product=product,
        user=request.user
    )

    if not created:
        like.delete()  # UNLIKE

    return redirect("product_detail", pk=pk)
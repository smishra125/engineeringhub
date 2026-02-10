from django.urls import path
from . import views

urlpatterns = [
    path("", views.product_list, name="product_list"),
    path("<int:pk>/", views.product_detail, name="product_detail"),
    path("<int:pk>/like/", views.product_like, name="product_like"),
]

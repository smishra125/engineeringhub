from django.urls import path
from .api import ProductListAPI, ProductDetailAPI

urlpatterns = [
    path('', ProductListAPI.as_view(), name='api_product_list'),
    path('<int:pk>/', ProductDetailAPI.as_view(), name='api_product_detail'),
]

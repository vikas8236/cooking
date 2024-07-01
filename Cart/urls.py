# urls.py
from django.urls import path
from .views import ProductAPI, AddToCartAPI, CartAPI

urlpatterns = [
    path('Cartproducts/', ProductAPI.as_view(), name='product_list'),
    path('cart/add/', AddToCartAPI.as_view(), name='add_to_cart'),
    path('cart/', CartAPI.as_view(), name='cart'),
]




















# from Cart.views import ProductAPI, CartAPI
# from django.urls import path

# urlpatterns = [
#     #...
#     path('cartproducts/', ProductAPI.as_view(), name='products'),
#     path('cartItems/', CartAPI.as_view(), name = "cart")

# ]


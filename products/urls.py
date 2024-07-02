# urls.py
from django.urls import path
from .views import ProductView, AddToCartView, RemoveFromCartView, CartView

urlpatterns = [
    path('product/', ProductView.as_view(), name = "products"),
    # path('register/', RegisterView.as_view(), name='register'),
    # path('login/', LoginView.as_view(), name = "login"),
    # path('user/', CurrentUserView.as_view(), name='current-user'),
    path('cart/add/', AddToCartView.as_view(), name='add-to-cart'),
    path('cart/remove/', RemoveFromCartView.as_view(), name='remove-from-cart'),
    path('cart/', CartView.as_view(), name='cart'),
]

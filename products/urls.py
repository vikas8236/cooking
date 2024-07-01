


from django.urls import path, include
from .views import AddToCartAPI, UpdateCartItemAPI, RemoveFromCartAPI, ViewCartAPI
from django.conf import settings
from django.conf.urls.static import static


from rest_framework.routers import DefaultRouter


router = DefaultRouter()

urlpatterns = [

    path('', include(router.urls)),
    # path('products/',ProductViewSet.as_view(), name = "products"),
    path('cart/', ViewCartAPI.as_view(), name='view-cart'),
    path('add_cart/', AddToCartAPI.as_view(), name='add-to-cart'),
    path('cart/update/<int:pk>/', UpdateCartItemAPI.as_view(), name='update-cart-item'),
    path('cart/remove/<int:pk>/', RemoveFromCartAPI.as_view(), name='remove-from-cart'),
]







if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



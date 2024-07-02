"""
URL configuration for crud_using_viewsets project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from rest_framework import permissions
# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi
from django.conf.urls.static import static
from django.conf import settings


# from django.contrib.auth.models import User
# from django_otp.admin import OTPAdminSite
# from django_otp.plugins.otp_totp.models import TOTPDevice
# from django_otp.plugins.otp_totp.admin import TOTPDeviceAdmin
from django.contrib.admin import AdminSite
# from . import models
# from products.models import Product, CartItem, Cart



# class OTPAdmin(OTPAdminSite):
#     pass  

# admin_site = OTPAdmin(name= 'OTPAdmin')
# admin_site.register(User)

# admin_site.register(TOTPDevice, TOTPDeviceAdmin)

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
    path('products/', include('products.urls')), 
    path('', include('Restaurants.urls')), 

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]























# -----------------------------------------------------
# from django.urls import path, include

# # from .admin import custom_otp_admin_site  # Import the custom OTP admin site

# urlpatterns = [
#     path('admin/', admin_site.urls),  # Use the custom OTP admin site
#     path('user/', include('user.urls')),
#     path('', include('products.urls')),
#     path('', include('Restaurants.urls')),
# ]














if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)







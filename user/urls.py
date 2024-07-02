from django.urls import path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from .views import RegisterView, LoginView
from django.urls import path
from .views import RegisterView



schema_view = get_schema_view(
    openapi.Info(
        title="cooking",
        default_version='v1',
        description="API Description",
        terms_of_service="https://www.example.com/policies/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),  # Or specify your permissions
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    # path('request-otp/', OTPRequestView.as_view(), name='request-otp'),
    # path('verify-otp/', OTPVerifyView.as_view(), name='verify-otp'),
    # path('generate-otp/', GenerateOTPView.as_view(), name='generate-otp'),
    # path('verify-otp/', VerifyOTPView.as_view(), name='verify-otp'),
]














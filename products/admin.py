from django.contrib import admin
from django_otp.admin import OTPAdminSite
from .models import Product, CartItem, Cart



admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CartItem)

# class CustomOTPAdminSite(OTPAdminSite, admin.AdminSite):
#     pass

# custom_otp_admin_site = CustomOTPAdminSite(name='custom_otp_admin')
# custom_otp_admin_site.register(Product)
# custom_otp_admin_site.register(Cart)
# custom_otp_admin_site.register(CartItem)




# # -------------------------------
# from django.contrib import admin
# from django_otp.admin import OTPAdminSite
# from .models import Product, CartItem, Cart
# from django.contrib.auth.models import User
# from django_otp.plugins.otp_totp.models import TOTPDevice
# from django_otp.plugins.otp_totp.admin import TOTPDeviceAdmin

# class CustomOTPAdminSite(OTPAdminSite, admin.AdminSite):
#     pass

# custom_otp_admin_site = CustomOTPAdminSite(name='custom_otp_admin')
# custom_otp_admin_site.register(Product)
# custom_otp_admin_site.register(Cart)
# custom_otp_admin_site.register(CartItem)
# custom_otp_admin_site.register(User)
# custom_otp_admin_site.register(TOTPDevice, TOTPDeviceAdmin)





# Register your models here.


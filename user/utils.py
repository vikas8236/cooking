# utils.py
import random
from datetime import datetime, timedelta

def generate_otp():
    return str(random.randint(100000, 999999))

def get_expiration_time():
    return datetime.now() + timedelta(minutes=5)  # OTP valid for 5 minutes


from django.core.mail import send_mail

def send_otp_via_email(email, otp):
    subject = 'Your OTP Code'
    message = f'Your OTP code is {otp}'
    send_mail(subject, message, 'from@example.com', [email])

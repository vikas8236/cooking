from django.db import models
# from django.contrib.auth.models import User
import random

class Student(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    age = models.IntegerField(default=18)
    email = models.EmailField(unique=True, )
    password = models.CharField(max_length=100) 
   
    def __str__(self):
        return self.email

from django.db import models
from django.contrib.auth.models import User
import uuid
from datetime import datetime, timedelta

class OTP(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()

    def is_valid(self):
        return datetime.now() < self.expires_at




  

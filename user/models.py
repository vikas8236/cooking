from django.db import models

class Student(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    # age = models.IntegerField(default=18)
    email = models.EmailField(unique=True )
    password = models.CharField(max_length=100) 
   
    def __str__(self):
        return self.email






  

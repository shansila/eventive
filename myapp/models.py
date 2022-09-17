
from django.db import models

# Create your models here.
class User(models.Model):
    Username=models.TextField(max_length=100)
    Email=models.TextField(max_length=100)
    Password=models.TextField(max_length=25)
    Phonenumber=models.TextField(max_length=25)
    Gender=models.TextField(max_length=25)


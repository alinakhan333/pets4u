
import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email_id = models.EmailField
    user_name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    phone_no = models.IntegerField
    ph_or_email = models.CharField 
    def __str__(self):
        return self.user_name

class Pet(models.Model):

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    age = models.DecimalField
    location = models.CharField
    image = models.ImageField
    type = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    

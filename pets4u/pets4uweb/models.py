
import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email_id = models.EmailField(max_length=255, null=True, blank=True)
    user_name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    phone_no = models.IntegerField(null=True)
    ph_or_email = models.CharField(max_length=20, default="Email")
    def __str__(self):
        return self.user_name

class Pet(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    age = models.DecimalField(max_digits=3, decimal_places=2, null=True)
    location = models.CharField(max_length=200, null=True)
    type = models.CharField(max_length=50)
    gender = models.CharField(max_length=20, null=True)
    def __str__(self):
        return self.name
    

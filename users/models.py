from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    phone_no = models.CharField(max_length=15, unique=True)
    full_name = models.CharField(max_length=150, default="Unknown")  

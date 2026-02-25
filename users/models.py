from django.db import models
from django.contrib.auth.models import AbstractUser
from users.managers import CustomUserManager
from django.conf import settings
import re


class User(AbstractUser):
    phone_number  = models.CharField(max_length=15, unique=True)
    is_phone_verified = models.BooleanField(default=False)
    otp = models.CharField(max_length=6)
    
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []
    
    # Phone numerber validation written in the manager file, so we can reuse it in both create_user and create_superuser methods.
    objects = CustomUserManager()
    
    
    
    
from django.db import models

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    avatar = models.ImageField(upload_to='user/%Y/', null=True)
    phone = models.CharField(max_length=15, blank=True)

    

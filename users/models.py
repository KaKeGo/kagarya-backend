from django.db import models
from django.utils import timezone
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser

# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self):
        pass
    def create_superuser(self):
        pass

class User(AbstractUser):
    username = models.CharField(max_length='40')
    email = models.EmailField(max_length='30', unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_created = models.DateTimeField(default=timezone.now)
    last_login = models.DateField(auto_now=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    objects = UserManager()
    
    def __str__(self):
        return self.email
    
    

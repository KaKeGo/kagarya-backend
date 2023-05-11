from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser

# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self):
        pass
    def create_superuser(self):
        pass

class User(AbstractUser):
    pass

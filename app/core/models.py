# Database Models

from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


class UserManger(BaseUserManager):

    # User can buy
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Please Provide a Valid Email.')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self.db)

        return user

    # User can buy and use the collecting software
    def create_user_collector(self, email, password, name):
        user = self.create_user(email, password)
        user.set_password(password)
        user.is_collector = True
        user.name = name
        user.save(using=self._db)

        return user

    # User can buy, sell, and use the collectiong software
    def create_user_seller(self, email, password, name):
        user = self.create_user(email, password)
        user.set_password(password)
        user.is_collector = True
        user.is_seller = True
        user.name = name
        user.save(using=self._db)

        return user

    # Admin User has all access
    def create_superuser(self, email, password):
        user =  self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.is_collector = True
        user.is_seller = True
        user.save(using=self._db)

        return user

    def change_user_collector(self, email, name):
        user = User.objects.get(email=email)
        user.is_collector = True


        return user

    def change_user_seller(self, email, name):
        user = User.objects.get(email=email)
        user.is_collector = True
        user.is_seller = True


        return user

class User(AbstractBaseUser, PermissionsMixin):
    # User in the Data base

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_collector = models.BooleanField(default=False)
    is_seller = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = UserManger()

    USERNAME_FIELD = 'email'

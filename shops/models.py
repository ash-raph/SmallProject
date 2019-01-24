from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

import os


def upload_posters_to(instance, filename):
    name = '{}_{}_{}'.format(instance.name, instance.distance, filename)
    return os.path.join('posters', name)


class Shop(models.Model):
    name = models.CharField(max_length=70, blank=True, null=True)
    distance = models.IntegerField(blank=True, null=True)
    poster = models.ImageField(upload_to=upload_posters_to, null=True, blank=True)


class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
    username = None
    email = models.EmailField(unique=True, blank=False, null=False)
    liked_shops = models.ManyToManyField(Shop, related_name='liked_by')
    disliked_shops = models.ManyToManyField(Shop, through='ShopUser', related_name='disliked_by')


class ShopUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='shop_user')
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='shop_user')
    disliked_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('shop', 'user')

from django.contrib.auth.models import AbstractUser
from django.db import models

import os


def upload_posters_to(instance, filename):
    name = '{}_{}_{}'.format(instance.name, instance.distance, filename)
    return os.path.join('posters', name)


class Shop(models.Model):
    name = models.CharField(max_length=70, blank=True, null=True)
    distance = models.IntegerField(blank=True, null=True)
    poster = models.ImageField(upload_to=upload_posters_to, null=True, blank=True)


class User(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', ]
    # override User.email:
    email = models.EmailField(unique=True, blank=False, null=False)
    shops = models.ManyToManyField(Shop, through='ShopUser', related_name='users')


class ShopUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='shop_user')
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='shop_user')
    disliked_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        unique_together = ('shop', 'user')

from django.contrib.auth.models import AbstractUser
from django.db import models


class Shops(models.Model):
    name = models.CharField(max_length=70, blank=True, null=True)
    distance = models.IntegerField(blank=True, null=True)


class User(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', ]
    # override User.email:
    email = models.EmailField(unique=True, blank=False, null=False)
    shops = models.ManyToManyField(Shops)






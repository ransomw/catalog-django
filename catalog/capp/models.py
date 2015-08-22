from django.db import models
from django.conf import settings


class Category(models.Model):
    name = models.CharField(max_length=80)


class Item(models.Model):
    title = models.CharField(max_length=80)
    description = models.CharField(max_length=250)
    category = models.ForeignKey(Category)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True)

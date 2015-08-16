from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=80)


class Item(models.Model):
    title = models.CharField(max_length=80)
    description = models.CharField(max_length=250)
    category = models.ForeignKey(Category)
    user = models.ForeignKey(User, null=True)

from django.db import models


class Product(models.Model):
    url = models.CharField(max_length=256)
    category = models.CharField(max_length=64)
    price = models.CharField(max_length=16)
    title = models.CharField(max_length=256)
    colors = models.TextField()
    images = models.TextField()
    description = models.TextField()

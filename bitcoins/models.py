from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=30)
    company = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=20,decimal_places=6)
    product_type = models.CharField(max_length=20)
    product_url = models.URLField()
    picture = models.URLField()

class Project(models.Model):
    name = models.CharField(max_length=30)
    project_url = models.URLField()
    author = models.CharField(max_length=20)
    picture = models.URLField()

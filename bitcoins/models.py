from django.db import models
from django.contrib.auth.models import User

# use this for field help:
# https://docs.djangoproject.com/en/1.6/ref/models/fields/#model-field-types

class Product(models.Model):
    name = models.CharField(max_length=30)
    company = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=20,decimal_places=8)
    product_type = models.CharField(max_length=20)
    product_description = models.TextField()
    product_url = models.URLField()
    picture = models.URLField()

class Project(models.Model):
    name = models.CharField(max_length=30)
    project_url = models.URLField()
    author = models.CharField(max_length=20)
    picture = models.URLField()

class Protocol(models.Model):
    name = models.CharField(max_length=30)
    company = models.CharField(max_length=30)
    author = models.CharField(max_length=20)
    protocol_description = models.TextField()
    protocol_url = models.URLField()
    picture = models.URLField()

class Coin(models.Model):
    name = models.CharField(max_length=30)
    coin_description = models.TextField()
    coin_hash_type = models.CharField(max_length=20)
    coin_url = models.URLField()
    picture = models.URLField()

class Asset(models.Model):
    name = models.CharField(max_length=30)
    asset_type = models.CharField(max_length=20)
    asset_ticker = models.CharField(max_length=30)
    asset_description = models.TextField()
    issuance_date = models.DateField()
    amount_issued = models.DecimalField(max_digits=20,decimal_places=8)
    price = models.DecimalField(max_digits=20,decimal_places=8)
    picture = models.URLField()
    company = models.CharField(max_length=30)

class Bounty(models.Model):
    name = models.CharField(max_length=30)
    amount = models.DecimalField(max_digits=20,decimal_places=8)
    bount_currency = models.CharField(max_length=30)
    bounty_type = models.CharField(max_length=20)
    bounty_description = models.TextField()
    bounty_url = models.URLField()
    picture = models.URLField()

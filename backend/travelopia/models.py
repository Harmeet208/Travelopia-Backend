# models.py

from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    email = models.EmailField()
    currency = models.IntegerField()
    travellers = models.IntegerField()

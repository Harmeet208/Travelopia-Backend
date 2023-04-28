# models.py

from django.db import models

class TravellerDetails(models.Model):
    name = models.CharField(max_length=255)
    destination_country = models.CharField(max_length=255)
    email = models.EmailField()
    budget_per_person = models.IntegerField()
    number_of_traveller = models.IntegerField()

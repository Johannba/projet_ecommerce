from django.db import models

class Address(models.Model):
    addresses = models.CharField(max_length=20)

    
class Country(models.Model):
      city = models.CharField(max_length=50)
      zip_code = models.CharField(max_length=5)
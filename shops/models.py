# shops/models.py
from django.contrib.auth import get_user_model
from django.db import models

class Shop(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    description = models.TextField()
    # Add other fields as needed

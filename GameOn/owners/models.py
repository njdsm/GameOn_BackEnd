from django.db import models

# Create your models here.


class Owner(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=250, blank=True, null=True)
    key = models.CharField(max_length=100, default="", blank=True, null=True)

from django.db import models

# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    user_name = models.CharField(max_length=20, null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)
    password = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    points = models.IntegerField(null=True, blank=True, default=0)
    host = models.BooleanField(default=False)
    logged_in = models.BooleanField(default=False)
    score = models.IntegerField(null=True, blank=True, default=0)
    is_playing = models.IntegerField(null=True, blank=True)

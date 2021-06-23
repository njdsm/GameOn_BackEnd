from django.db import models

# Create your models here.


class Stat(models.Model):
    player = models.ForeignKey('users.User', blank=True, null=True, on_delete=models.CASCADE)
    placement = models.IntegerField(blank=True, null=True)

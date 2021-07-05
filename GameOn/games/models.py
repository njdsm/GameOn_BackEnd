from django.db import models

# Create your models here.


class Game(models.Model):
    owner = models.ForeignKey('owners.Owner', blank=True, null=True, on_delete=models.CASCADE)
    player_min = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=250, blank=True, null=True)
    is_active = models.BooleanField(default=False)

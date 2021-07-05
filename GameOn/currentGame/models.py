from django.db import models

# Create your models here.


class CurrentGame(models.Model):
    player_id = models.IntegerField(blank=True, null=True)
    user_name = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)

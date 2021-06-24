from django.db import models

# Create your models here.


class Stat(models.Model):
    game = models.ForeignKey('games.Game', blank=True, null=True, on_delete=models.CASCADE)
    player = models.ForeignKey('users.User', blank=True, null=True, on_delete=models.CASCADE)
    placement = models.IntegerField(blank=True, null=True)

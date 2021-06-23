from django.db import models

# Create your models here.


class UserRoles(models.Model):
    user = models.ForeignKey('users.User', blank=True, null=True, on_delete=models.CASCADE)
    role = models.ForeignKey('roles.Role', blank=True, null=True, on_delete=models.CASCADE)


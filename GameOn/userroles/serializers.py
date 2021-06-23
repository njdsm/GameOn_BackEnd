from rest_framework import serializers
from .models import UserRoles


class UserRolesSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserRoles
        fields = ['user', 'role']

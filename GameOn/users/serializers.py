from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'user_name', 'email', 'password', 'phone', 'points', 'host', 'logged_in', 'score', 'is_playing']

from rest_framework import serializers
from .models import Game


class GameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Game
        fields = ['id', 'owner', 'player_min', 'name', 'description', 'is_active']

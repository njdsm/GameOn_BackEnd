from rest_framework import serializers
from .models import CurrentGame


class GameSerializer(serializers.ModelSerializer):

    class Meta:
        model = CurrentGame
        fields = ['player_id', 'user_name', 'phone']

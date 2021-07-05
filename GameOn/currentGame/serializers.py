from rest_framework import serializers
from .models import CurrentGame, Answers


class GameSerializer(serializers.ModelSerializer):

    class Meta:
        model = CurrentGame
        fields = ['player_id', 'user_name', 'phone']


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answers
        fields = ['answer', 'phone']

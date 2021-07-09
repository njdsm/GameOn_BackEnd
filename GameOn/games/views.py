from .models import Game
from .serializers import GameSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

# Create your views here.


class GamesList(APIView):

    def get(self, request):
        game = Game.objects.all()
        serializer = GameSerializer(game, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = GameSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class GamesDetail(APIView):

    def get_game(self, pk):
        try:
            return Game.objects.all().filter(owner=pk)
        except Game.DoesNotExist:
            raise Http404

    def start_game(self, pk):
        try:
            return Game.objects.get(pk=pk)
        except Game.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        game = self.get_game(pk)
        serializer = GameSerializer(game, many=True)
        return Response(serializer.data)

    def put(self, request, pk):
        game = self.start_game(pk)
        serializer = GameSerializer(game, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        game = self.get_game(pk)
        game.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

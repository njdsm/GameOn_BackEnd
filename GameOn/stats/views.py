from .models import Stat
from .serializers import StatSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

# Create your views here.


class StatsList(APIView):

    def get_stats_player(self, fk):
        try:
            return Stat.objects.filter(player_id=fk)
        except Stat.DoesNotExist:
            return Response(Http404)

    def get_stats_game(self, fk):
        try:
            return Stat.objects.filter(game_id=fk)
        except Stat.DoesNotExist:
            return Response(Http404)

    def get_specific_stat(self, pk):
        try:
            return Stat.objects.get(pk=pk)
        except Stat.DoesNotExist:
            return Response(Http404)

    def get(self, request):
        stats = ""
        try:
            if request.query_params['game_id']:
                stats = self.get_stats_game(int(request.query_params['game_id']))
        except:
            pass
        try:
            if request.query_params['player_id']:
                stats = self.get_stats_player(int(request.query_params['player_id']))
        except:
            pass
        try:
            if request.query_params['stat']:
                stats = self.get_specific_stat(int(request.query_params['stat']))
        except:
            pass
        if stats == "":
            stats = Stat.objects.all()
        serializer = StatSerializer(stats, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class StatsDetail(APIView):



    # def put(self, request, pk):
    #     pass
    #
    def delete(self, request, pk):
        stat = self.get_specific_stat(pk)
        stat.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
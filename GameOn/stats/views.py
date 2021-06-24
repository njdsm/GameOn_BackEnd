from .models import Stat
from .serializers import StatSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

# Create your views here.


class StatsList(APIView):

    def get(self, request):
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

    def get_stats(self, fk):
        try:
            return Stat.objects.get(fk=fk, many=True)
        except Stat.DoesNotExist:
            raise Http404

    def get_specific_stat(self, pk):
        try:
            return Stat.objects.get(pk=pk)
        except Stat.DoesNotExist:
            raise Http404

    def get(self, pk):
        stats = self.get_stats(pk)
        serializer = StatSerializer(stats)
        return Response(serializer.data)

    # def put(self, request, pk):
    #     pass
    #
    def delete(self, request, pk):
        stat = self.get_specific_stat(pk)
        stat.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
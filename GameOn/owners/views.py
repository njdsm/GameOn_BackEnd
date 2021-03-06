from .models import Owner
from .serializers import OwnerSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

# Create your views here.


class OwnersList(APIView):

    def get(self, request):
        owner = Owner.objects.all()
        serializer = OwnerSerializer(owner, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = OwnerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class OwnersDetail(APIView):

    def get_owner(self, key):
        try:
            return Owner.objects.get(key=key)
        except Owner.DoesNotExist:
            raise Http404

    def get(self, request, key):
        owner = self.get_owner(key)
        serializer = OwnerSerializer(owner)
        return Response(serializer.data)

    def put(self, request, key):
        owner = self.get_owner(key)
        serializer = OwnerSerializer(owner, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        owner = self.get_Owner(pk)
        owner.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

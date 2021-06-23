from .models import Role
from .serializers import RoleSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

# Create your views here.


class RolesList(APIView):
    pass
#
#     def get(self, request):
#         pass
#         # return Response(serializer.data)
#
#     def post(self, request):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
#
#
class RolesDetail(APIView):
    pass
#     def get_cards(self, pk):
#         try:
#             return Collection.objects.get(pk=pk)
#         except Collection.DoesNotExist:
#             raise Http404
#
#     def get_collection(self, pk):
#         try:
#             return Collection.objects.get(pk=pk)
#         except Collection.DoesNotExist:
#             raise Http404
#
#     def get(self, pk):
#         collection = self.get_collection(pk)
#         serializer = UserSerializer(collection)
#         return Response(serializer.data)
#
#     def put(self, request, pk):
#         pass
#
#     def delete(self, request, pk):
#         collection = self.get_collection(pk)
#         collection.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

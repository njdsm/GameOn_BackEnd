from .models import CurrentGame as Game
from .models import Answers
from .serializers import GameSerializer, AnswerSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from twilio.rest import Client
from .API import twilio_sid, twilio_auth


# Create your views here.
class TwilioList(APIView):

    def post(self, request):
        account_sid = twilio_sid
        auth_token = twilio_auth
        client = Client(account_sid, auth_token)
        if "REDEEM" in request.data:
            client.messages.create(
                body="Show this when you go to pay your bill to receive a discount worth " + str(request.data["question"]["REDEEM"]) + " points!",
                from_='+13126266151',
                to='+1' + request.data["user"]["phone"]
            )
            return Response(status=status.HTTP_200_OK)
        elif "question" in request.data:
            client.messages.create(
                body=request.data["question"]["question"],
                from_='+13126266151',
                to='+1' + request.data["user"]["phone"],
            )
            return Response(status=status.HTTP_200_OK)
        elif "JOIN" in request.data:
            print("JOIN")
        else:
            client.messages.create(
                body="We got your answer!",
                from_='+13126266151',
                to=request.data["From"],
            )

            payload = {
                "answer": request.data["Body"],
                "phone": request.data["From"]
            }
            serializer = AnswerSerializer(data=payload)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class AnswersList(APIView):

    def get(self, request):
        answers = Answers.objects.all()
        serializer = AnswerSerializer(answers, many=True)
        return Response(serializer.data)


class AnswersDetails(APIView):

    def get_answer(self, pk):
        try:
            return Answers.objects.get(pk=pk)
        except Answers.DoesNotExist:
            raise Http404

    def delete(self, request, pk):
        answer = self.get_answer(pk)
        answer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CurrentGamesList(APIView):

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

    def delete(self, request):
        Game.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CurrentGamesDetail(APIView):

    def get_game(self, pk):
        try:
            return Game.objects.get(pk=pk)
        except Game.DoesNotExist:
            raise Http404

    def get(self, pk):
        game = self.get_game(pk)
        serializer = GameSerializer(game)
        return Response(serializer.data)

    def put(self, request, pk):
        game = self.get_game(pk)
        serializer = GameSerializer(game, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        game = self.get_game(pk)
        game.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import QuestionsSerializer, ChoicesSerializer

# Create your views here.


from .models import Question, Choice

# Get questions and display them


@api_view(['GET'])
def sayHello(request):
    return Response('hello')

@api_view(['GET'])
def getQuestions(request):
    questions= Question.objects.all()
    serializer= QuestionsSerializer(many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getChoices(request):
    questions= Choice.objects.all()
    serializer= ChoicesSerializer(many=True)
    return Response(serializer.data)





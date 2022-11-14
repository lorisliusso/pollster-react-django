from rest_framework import serializers
from .models import Question, Choice


class QuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model= Question
        fields= '__all__'

class ChoicesSerializer(serializers.ModelSerializer):
    class Meta:
        model= Choice
        fields= '__all__'
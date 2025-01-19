from rest_framework import serializers

from apps.chats.models import Answer


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        exclude = ("question",)

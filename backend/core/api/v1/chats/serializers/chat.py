from .question import ChatQuestionAnswersSerializer

from rest_framework import serializers

from apps.chats.models import Chat


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = "__all__"


class UpdateChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ("name",)


class SubnetChatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = (
            "name",
            "id",
        )


class ChatMessagesSerializer(serializers.ModelSerializer):
    messages = ChatQuestionAnswersSerializer(
        source="questions", many=True, read_only=True
    )
    subnet = serializers.CharField(source="subnet.name", read_only=True)

    class Meta:
        model = Chat
        fields = (
            "id",
            "name",
            "user",
            "subnet",
            "created_at",
            "messages",
        )

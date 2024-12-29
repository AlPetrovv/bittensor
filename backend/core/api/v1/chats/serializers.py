from drf_spectacular.utils import extend_schema_field

from rest_framework import serializers

from api.v1.chats.services import make_answers
from apps.chats.models import Answer
from apps.chats.models import Chat
from apps.chats.models import Question


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = "__all__"


class SubnetChatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = (
            "name",
            "id",
        )


class UpdateChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ("name",)


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        exclude = ("question",)


class ChatQuestionAnswersSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = (
            "id",
            "text",
            "created_at",
            "answers",
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


class QuestionAnswerSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    answers = serializers.SerializerMethodField()

    class Meta:
        model = Question
        fields = ("id", "text", "user", "chat", "created_at", "answers")

    @extend_schema_field(AnswerSerializer(many=True))
    def get_answers(self, obj) -> list[dict[str, str]]:
        # get data for api request
        chat = (
            Chat.objects.select_related("subnet", "user")
            .prefetch_related("questions", "questions__answers")
            .get(id=obj.chat.id)
        )
        answers = make_answers(chat)

        return [
            {"id": ans.id, "text": ans.text, "created_at": ans.created_at}
            for ans in answers
        ]  # todo make entities

from drf_spectacular.utils import extend_schema_field

from .answer import AnswerSerializer
from rest_framework import serializers

from apps.chats.models import Question, Chat
from ..services import make_answers


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"


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


class QuestionAnswerSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    answers = serializers.SerializerMethodField()

    class Meta:
        model = Question
        fields = ("id", "text", "user", "chat", "created_at", "answers")

    @extend_schema_field(AnswerSerializer(many=True))
    def get_answers(self, obj) -> list[dict[str, str]]:
        chat = (
            Chat.objects.select_related("subnet", "user")
            .prefetch_related("questions", "questions__answers")
            .get(id=obj.chat.id)
        )  # get data for api request
        answers = make_answers(chat)

        return [
            {"id": ans.id, "text": ans.text, "created_at": ans.created_at}
            for ans in answers
        ]  # todo make entities

from rest_framework import mixins
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from apps.chats.models import Chat
from apps.chats.models import Question
from .serializers.chat import (
    ChatSerializer,
    UpdateChatSerializer,
    ChatMessagesSerializer,
)
from .serializers.question import QuestionAnswerSerializer

from ...base.mixins import SerializerByActionMixin
from ...base.permissions import IsOwnerOrAdmin


class ChatsViewSet(
    SerializerByActionMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet,
):
    serializer_class = ChatSerializer
    queryset = Chat.objects.all()
    serializer_class_by_action = {
        "partial_update": UpdateChatSerializer,
        "messages": ChatMessagesSerializer,
    }
    permission_classes = [
        IsOwnerOrAdmin,
    ]
    http_method_names = ["get", "post", "patch", "delete"]

    @action(methods=["get"], detail=True, permission_classes=permission_classes)
    def messages(self, request, *args, **kwargs):
        """Get messages from chat"""
        chat = self.get_object()
        serializer = self.get_serializer(chat, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)


class QuestionsViewSet(mixins.CreateModelMixin, GenericViewSet):
    permission_classes = [
        IsOwnerOrAdmin,
    ]
    serializer_class = QuestionAnswerSerializer
    queryset = Question.objects.all()

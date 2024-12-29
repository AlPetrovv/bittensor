from rest_framework import mixins
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.chats.models import Chat
from apps.subnets.models import Subnet

from ...base.mixins import SerializerByActionMixin
from ..chats.serializers import SubnetChatsSerializer
from .serializers import SubnetSerializer


class SubnetViewSet(
    SerializerByActionMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
    queryset = Subnet.objects.all()
    serializer_class = SubnetSerializer
    permission_classes = [AllowAny]
    serializer_class_by_action = {
        "chats": SubnetChatsSerializer,
    }
    lookup_field = "slug"

    @action(methods=["get"], detail=True, permission_classes=[IsAuthenticated])
    def chats(self, request, *args, **kwargs):
        subnet = self.get_object()
        user = request.user
        chats = Chat.objects.filter(subnet=subnet, user=user)
        serializer = self.get_serializer(chats, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

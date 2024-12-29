from rest_framework.viewsets import ModelViewSet

from api.base.mixins import SerializerByActionMixin


class BaseViewSet(SerializerByActionMixin, ModelViewSet): ...

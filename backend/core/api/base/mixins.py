class SerializerByActionMixin:
    """The class which selects specific serializer class for specific action"""

    def get_serializer_class(self):
        try:
            return self.serializer_class_by_action[self.action]
        except (KeyError, AttributeError):
            return self.serializer_class

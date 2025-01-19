from rest_framework.permissions import BasePermission


class IsOwnerOrAdmin(BasePermission):
    """
    Custom permission to only allow owners of an object or admin to edit it.
    """

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user or request.user.is_superuser

    def has_permission(self, request, view):
        return request.user.is_authenticated or request.user

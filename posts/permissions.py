from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    # for ist view
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False

    # for details view
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user

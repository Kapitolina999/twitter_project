from rest_framework import permissions


class AdminOrOwnerPermission(permissions.BasePermission):
    message = 'You don\'t have permission to edit'

    def has_object_permission(self, request, view, obj):
        return bool(request.user == obj.author or request.user.is_staff)
from rest_framework import permissions

class UserPermissons(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.pk == request.user.pk

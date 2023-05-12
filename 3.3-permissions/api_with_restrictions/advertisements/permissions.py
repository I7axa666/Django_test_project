from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser == True or request.method == 'GET':
            return True

        return request.user.id == obj.creator_id

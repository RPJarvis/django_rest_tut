from rest_framework import  permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """ allow only object owners to edit
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        #return true false if object belongs to suer making request
        return obj.owner == request.user
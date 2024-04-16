from rest_framework import permissions

    
class IsContributorOrOwner(permissions.BasePermission):
     def has_object_permission(self, request, view, obj):
        METHODS = permissions.SAFE_METHODS + ('POST',)
        if request.method in METHODS:
            return obj.get_contributors().filter(user=request.user).exists()
        elif request.method in ('PUT', 'PATCH', 'DELETE'):
            return obj.author == request.user
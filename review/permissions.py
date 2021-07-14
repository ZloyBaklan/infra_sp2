from rest_framework.permissions import SAFE_METHODS, BasePermission
from users.models import CustomUser


class IsOwnerAdminModeratorToEdit(BasePermission):
    def has_object_permission(self, request, view, obj):
        return (
            request.method in SAFE_METHODS
            or request.user.role in (
                [CustomUser.UserRoles.MODERATOR, CustomUser.UserRoles.ADMIN]
            )
            or request.user.is_superuser
            or request.user == obj.author
        )

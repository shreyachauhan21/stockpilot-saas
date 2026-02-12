from rest_framework.permissions import BasePermission

class IsRole(BasePermission):
    allowed_roles = []

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and
            request.user.role in self.allowed_roles
        )


class IsAdmin(IsRole):
    allowed_roles = ["ADMIN"]


class IsManager(IsRole):
    allowed_roles = ["MANAGER"]


class IsStaff(IsRole):
    allowed_roles = ["STAFF"]

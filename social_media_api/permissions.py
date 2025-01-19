from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrIfAuthenticatedReadOnly(BasePermission):
    def has_permission(self, request, view):
        return bool(
            (
                request.method in SAFE_METHODS
                and request.user
                and request.user.is_authenticated
            )
            or (request.user and request.user.is_staff)
        )


class AllowListAndCreateOnly(BasePermission):
    def has_permission(self, request, view):
        return bool(
            (
                request.method in SAFE_METHODS
                or request.method == "POST"
            )
        )


class IsAuthenticatedAndOwnProfile(BasePermission):
    def has_permission(self, request, view):
        if request.method == "POST":
            return request.user and request.user.is_authenticated
        return True

    def has_object_permission(self, request, view, obj):
        if request.method in ["PUT", "PATCH", "DELETE"]:
            return obj == request.user.profile
        return True

    def perform_create(self, serializer):
        if hasattr(self.request.user, 'profile'):
            serializer.save(user=self.request.user)

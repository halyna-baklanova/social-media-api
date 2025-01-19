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
        # Дозволяємо створювати профіль, якщо користувач аутентифікований
        if request.method == "POST":
            return request.user and request.user.is_authenticated
        return True  # Для інших методів (GET, PUT, PATCH, DELETE) дозволяємо лише власні профілі

    def has_object_permission(self, request, view, obj):
        # Для методів редагування перевіряємо, чи це власний профіль
        if request.method in ["PUT", "PATCH", "DELETE"]:
            return obj == request.user.profile  # Припускаємо, що профіль зберігається у зв'язку з користувачем
        return True

    def perform_create(self, serializer):
        # Для методу POST встановлюємо поточного користувача в поле User
        if hasattr(self.request.user, 'profile'):
            # Встановлюємо користувача як автора профілю
            serializer.save(user=self.request.user)

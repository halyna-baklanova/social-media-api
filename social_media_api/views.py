from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets, mixins, status
from .models import Profile, Post
from .permissions import IsAuthenticatedAndOwnProfile
from .serializers import ProfileSerializer, PostSerializer, ProfileListSerializer, ProfileDetailSerializer


class ProfileViewSet(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        if Profile.objects.filter(user=request.user).exists():
            return Response({"detail": "Profile already exists."}, status=status.HTTP_400_BAD_REQUEST)
        return super().create(request, *args, **kwargs)






        # def get_queryset(self):
    #     # Повертаємо всі профілі для всіх користувачів
    #     return Profile.objects.all()
    #
    # def perform_create(self, serializer):
    #     # Прив'язуємо профіль до поточного користувача без перевірки наявності
    #     serializer.save(user=self.request.user)

    # def get_queryset(self):
    #     return Profile.objects.filter(user=self.request.user)
    #
    # def get_serializer_class(self):
    #     if self.action == "list":
    #         return ProfileListSerializer
    #     if self.action == "retrieve":
    #         return ProfileDetailSerializer
    #     return self.serializer_class




    # def get_queryset(self):
    #     return Profile.objects.filter(user=self.request.user)
    #
    # def list(self, request, *args, **kwargs):
    #     return super().list(request, *args, **kwargs)

    # def create(self, request, *args, **kwargs):
    #     if Profile.objects.filter(user=request.user).exists():
    #         return Response(
    #             {"detail": "Ви вже маєте профіль."},
    #             status=status.HTTP_400_BAD_REQUEST,
    #         )
    #     return super().create(request, *args, **kwargs)
    #
    # def list(self, request, *args, **kwargs):
    #     return super().list(request, *args, **kwargs)


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        hashtags = self.request.query_params.get("hashtags", None)
        if hashtags:
            hashtags = hashtags.split(",")
            queryset = queryset.filter(hashtags__name__in=hashtags).distinct()
        return queryset

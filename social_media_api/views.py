from rest_framework import viewsets

from .models import Profile, Post
from .serializers import ProfileSerializer, PostSerializer


class ProfileView(viewsets.ModelViewSet):
    model = Profile
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

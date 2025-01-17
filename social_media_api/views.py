from rest_framework import viewsets

from .models import Profile
from .serializers import ProfileSerializer


class ProfileListView(viewsets.ModelViewSet):
    model = Profile
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

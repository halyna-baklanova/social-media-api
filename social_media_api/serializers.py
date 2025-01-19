from rest_framework import serializers, status
from rest_framework.response import Response

from social_media_api.models import (
    Profile,
    Post,
    Hashtag,
)
from user.serializers import UserSerializer


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Profile
        fields = ["id", "user", "full_name", "bio", "registration_date"]


class ProfileListSerializer(ProfileSerializer):
    class Meta:
        model = Profile
        fields = ("id", "bio", "user", "full_name", "registration_date")

        def list(self, request, *args, **kwargs):
            # Просто повертаємо список всіх профілів
            profiles = Profile.objects.all()
            serializer = self.get_serializer(profiles, many=True)
            return Response(serializer.data)


class ProfileDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ("id", "user", "full_name", "bio", "registration_date")


    # def create(self, validated_data):
    #     user = self.context["request"].user
    #     return Profile.objects.create(user=user, **validated_data)



# class ProfileDetailSerializer(ProfileSerializer):
#     posts = ProfileSerializer(many=True, read_only=True)
#     class Meta:
#         model = Profile
#         fields = ["id", "user", "full_name", "bio", "registration_date"]


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"


class HashtagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hashtag
        fields = ["name"]

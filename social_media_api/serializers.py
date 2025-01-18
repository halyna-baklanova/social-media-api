from rest_framework import serializers

from social_media_api.models import (
    Profile,
    Post,
    Hashtag,
)


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ["id", "user", "full_name", "bio", "registration_date"]


class ProfileDetailSerializer(ProfileSerializer):
    posts = ProfileSerializer(many=True, read_only=True)
    class Meta:
        model = Profile
        fields = ["id", "user", "full_name", "bio", "registration_date"]


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"


class HashtagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hashtag
        fields = ["name"]

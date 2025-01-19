import pathlib
import uuid

from django.db import models

from django.utils.timezone import now
from django.utils.text import slugify
from django.contrib.auth.models import AbstractUser

from user.models import User

def actor_photo_path(instance: "Profile", filename: str) -> pathlib.Path:
    extension = pathlib.Path(filename).suffix
    filename = f"{slugify(instance.last_name)}-{uuid.uuid4()}" + extension
    return pathlib.Path("uploads/avatars/") / pathlib.Path(filename)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    full_name = models.CharField(max_length=100)
    bio = models.CharField(max_length=255, null=True, blank=True)
    avatar = models.ImageField(null=True, upload_to="uploads/")
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name}"


class Post(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(default=now)
    hashtags = models.ManyToManyField("Hashtag", related_name="posts", blank=True)

    def __str__(self):
        return self.text


class Like(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name="likes", on_delete=models.CASCADE)


class Hashtag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Comment(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

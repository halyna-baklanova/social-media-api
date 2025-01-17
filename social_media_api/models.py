from django.utils.timezone import now

from django.db import models


class Profile(models.Model):
    bio = models.CharField(max_length=255)
    name = models.CharField(max_length=255, null=True)
    registration_date = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"


class Post(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return self.text

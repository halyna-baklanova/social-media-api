from django.db import models
from django.contrib import admin


class Profile(models.Model):
    bio = models.CharField(max_length=255)
    name = models.CharField(max_length=255, null=True)
    registration_date = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"


class Post(models.Model):
    pass


class Comment(models.Model):
    pass

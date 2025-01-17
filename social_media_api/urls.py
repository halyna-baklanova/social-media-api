from django.urls import path, include
from rest_framework import routers

from social_media_api.views import ProfileView, PostViewSet


router = routers.DefaultRouter()
router.register("profiles", ProfileView)
router.register("posts", PostViewSet)
urlpatterns = [path("", include(router.urls))]

app_name = "socialmedia"

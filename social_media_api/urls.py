from django.urls import path, include
from rest_framework import routers

from social_media_api.views import ProfileListView


router = routers.DefaultRouter()
router.register("profiles", ProfileListView)
urlpatterns = [path("", include(router.urls))]

app_name = "socialmedia"

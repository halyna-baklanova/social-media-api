from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["id", "full_name", "bio", "registration_date", ]
    search_fields = ["full_name", ]
    list_filter = ["full_name", ]

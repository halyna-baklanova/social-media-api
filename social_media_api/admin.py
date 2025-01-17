from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["id", "bio", "name", "registration_date", ]
    search_fields = ["name", ]
    list_filter = ["name", ]

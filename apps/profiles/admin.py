from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "pkid",
        "user",
        "gender",
        "country",
        "state",
    ]
    list_filter = ["gender", "country"]
    list_display_links = ["id", "pkid", "user"]


admin.site.register(Profile, ProfileAdmin)

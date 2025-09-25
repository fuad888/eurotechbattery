from django.contrib import admin
from Home.models import Homepage


@admin.register(Homepage)
class HomepageAdmin(admin.ModelAdmin):
    list_display = ("id", "image_left", "image_right")
    list_display_links = ("id",)

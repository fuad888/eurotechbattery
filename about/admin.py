from django.contrib import admin
from about.models import Aboutpage,About,team
from parler.admin import TranslatableAdmin

@admin.register(Aboutpage)
class AboutpageAdmin(TranslatableAdmin):
    list_display = ("get_title", "hero_photo")
    search_fields = ("translations__title",)

    def get_title(self, obj):
        return obj.safe_translation_getter("title", any_language=True)
    get_title.short_description = "Title"

@admin.register(About)
class AboutAdmin(TranslatableAdmin):
    list_display = ("get_company_story", "get_mission", "get_vision", "created_at", "updated_at")
    search_fields = ("translations__company_story", "translations__mission", "translations__vision")

    def get_company_story(self, obj):
        return obj.safe_translation_getter("company_story", any_language=True)
    get_company_story.short_description = "Company Story"

    def get_mission(self, obj):
        return obj.safe_translation_getter("mission", any_language=True)
    get_mission.short_description = "Mission"

    def get_vision(self, obj):
        return obj.safe_translation_getter("vision", any_language=True)
    get_vision.short_description = "Vision"

@admin.register(team)
class teamAdmin(TranslatableAdmin):
    list_display = ("get_name", "get_position", "photo")
    search_fields = ("translations__name", "translations__position")

    def get_name(self, obj):
        return obj.safe_translation_getter("name", any_language=True)
    get_name.short_description = "Name"

    def get_position(self, obj):
        return obj.safe_translation_getter("position", any_language=True)
    get_position.short_description = "Position"

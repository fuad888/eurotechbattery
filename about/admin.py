from django.contrib import admin
from about.models import Aboutpage,About,team
from parler.admin import TranslatableAdmin

@admin.register(Aboutpage)
class AboutpageAdmin(TranslatableAdmin):

    list_display = ('title',)
    search_fields = ('title',)

@admin.register(About)
class AboutAdmin(TranslatableAdmin):

    list_display = ('company_story','mission', 'vision', 'created_at', 'updated_at',)
    search_fields = ('mission', 'vision')
    readonly_fields = ('created_at', 'updated_at')

@admin.register(team)
class TeamAdmin(TranslatableAdmin):

    list_display = ('name', 'position','photo',)
    search_fields = ('name', 'position',)
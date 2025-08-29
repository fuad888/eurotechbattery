from django.contrib import admin
from .models import Setting


# Register your models here.
@admin.register(Setting)
class SettingAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'email', 'phone', 'postal_code')
    search_fields = ('email', 'phone', 'postal_code', 'address')
    fieldsets = (
        (None, {
            'fields': ('logo', 'title', 'email', 'phone', 'postal_code', 'address')
        }),
        ('Social Media', {
            'fields': ('facebook', 'instagram', 'twitter', 'pinterest')
        }),
        ('Newsletter', {
            'fields': ('newsletter', 'newsletter_description')
        }),
    )
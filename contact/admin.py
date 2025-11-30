from django.contrib import admin
from contact.models import contactmessage, FAQ, herosection
from parler.admin import TranslatableAdmin

@admin.register(contactmessage)
class contactmessageAdmin(TranslatableAdmin):

    list_display = ('name', 'email', 'phone', 'interest')
    search_fields = ('name', 'email', 'phone', 'interest')
    list_filter = ('interest',)

@admin.register(FAQ)
class FAQAdmin(TranslatableAdmin):
    list_display = ('question', 'created_at', 'updated_at')
    search_fields = ('translations__question', 'translations__answer')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        (None, {
            'fields': ('question', 'answer')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('translations')
    
@admin.register(herosection)
class herosectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle')
    search_fields = ('title', 'subtitle')
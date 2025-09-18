from django.contrib import admin
from .models import Setting


# Register your models here.
from django.contrib import admin
from .models import Setting

@admin.register(Setting)
class SettingAdmin(admin.ModelAdmin):
    # Admin siyahısında göstəriləcək sahələr
    list_display = ('title', 'email', 'phone', 'mobile')
    
    # Axtarış sahələri
    search_fields = ('title', 'email', 'phone')
    
    # Read-only sahələr (məsələn logo sahəsini dəyişmədən göstərmək üçün)
    readonly_fields = ()

    # Field-ları qruplaşdırmaq
    fieldsets = (
        (None, {
            'fields': (
                'logo',
                'title',
                'email',
                'phone',
                'mobile',
                'postal_code',
                'address1',
                'address2',
                'facebook',
                'instagram',
                'newsletter',
                'newsletter_description',
            )
        }),
    )

    # Add və delete əməliyyatlarını disable etmək
    def has_add_permission(self, request):
        if not request.user.is_superuser:
            return False
        return True

    def has_delete_permission(self, request, obj=None):
        if not request.user.is_superuser:
            return False
        return True

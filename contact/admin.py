from django.contrib import admin
from contact.models import contactmessage
from parler.admin import TranslatableAdmin

@admin.register(contactmessage)
class contactmessageAdmin(TranslatableAdmin):

    list_display = ('name', 'email', 'phone', 'interest')
    search_fields = ('name', 'email', 'phone', 'interest')
    list_filter = ('interest',)
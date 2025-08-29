from django.contrib import admin
from .models import Category, Product
from parler.admin import TranslatableAdmin

# Register your models here.
@admin.register(Category)
class CategoryAdmin(TranslatableAdmin):
    list_display = ('__str__',)
    search_fields = ('translations__name',)
    fieldsets = (
        (None, {
            'fields': ('name', 'description')
        }),
    )

@admin.register(Product)
class ProductAdmin(TranslatableAdmin):
    list_display = ('__str__', 'price', 'stock', 'available', 'created', 'updated')
    list_filter = ('available', 'created', 'updated')
    search_fields = ('translations__name', 'translations__description')
    readonly_fields = ('slug', 'created', 'updated')
    fieldsets = (
        (None, {
            'fields': ('name', 'description', 'price', 'stock', 'available', 'image', 'slug', 'Category')
        }),
        ('Timestamps', {
            'fields': ('created', 'updated'),
            'classes': ('collapse',),
        }),
    )
    readonly_fields = ('created', 'updated')

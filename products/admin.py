from django.contrib import admin
from parler.admin import TranslatableAdmin
from products.models import Category, Products



@admin.register(Category)
class CategoryAdmin(TranslatableAdmin):
    list_display = ("get_name", "parent", "slug")
    search_fields = ("translations__name",)

    def get_name(self, obj):
        return obj.safe_translation_getter("name", any_language=True)
    get_name.short_description = "Category Name"

    def get_prepopulated_fields(self, request, obj=None):
        return {"slug": ("name",)}



@admin.register(Products)
class ProductsAdmin(TranslatableAdmin):
    list_display = ("get_name", "category", "price", "created_at")
    list_filter = ("category",)
    search_fields = ("translations__name",)

    def get_name(self, obj):
        return obj.safe_translation_getter("name", any_language=True)
    get_name.short_description = "Product Name"

    def get_prepopulated_fields(self, request, obj=None):
        return {"slug": ("name",)}


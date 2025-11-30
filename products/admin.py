from django.contrib import admin
from parler.admin import TranslatableAdmin
from products.models import Category, Products, ParentCategory,Productpage

@admin.register(Productpage)
class ProductPageAdmin(TranslatableAdmin):
    list_display = ("hero_title", "hero_subtitle", "hero_image")
    search_fields = ("translations__title",)

    def get_title(self, obj):
        return obj.safe_translation_getter("title", any_language=True)
    get_title.short_description = "Page Title"

    def get_prepopulated_fields(self, request, obj=None):
        return {"slug": ("title",)}

@admin.register(Category)
class CategoryAdmin(TranslatableAdmin):
    list_display = ("get_name", "slug")
    search_fields = ("translations__name",)

    def get_name(self, obj):
        return obj.safe_translation_getter("name", any_language=True)
    get_name.short_description = "Category Name"

    def get_prepopulated_fields(self, request, obj=None):
        return {"slug": ("name",)}
    
@admin.register(ParentCategory)
class ParentCategoryAdmin(TranslatableAdmin):
    list_display = ("get_name", "slug")
    search_fields = ("translations__name",)

    def get_name(self, obj):
        return obj.safe_translation_getter("name", any_language=True)
    get_name.short_description = "Parent Category Name"

    def get_prepopulated_fields(self, request, obj=None):
        return {"slug": ("name",)}



@admin.register(Products)
class ProductsAdmin(TranslatableAdmin):
    list_display = ("get_name", "category", "price", "created_at","pdf","voltage","model_number","amperage",)
    list_filter = ("category",)
    search_fields = ("translations__name",)

    def get_name(self, obj):
        return obj.safe_translation_getter("name", any_language=True)
    get_name.short_description = "Product Name"

    def get_prepopulated_fields(self, request, obj=None):
        return {"slug": ("name",)}


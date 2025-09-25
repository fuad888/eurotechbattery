from django.db import models
from django.utils.text import slugify
from parler.models import TranslatableModel, TranslatedFields


from django.db import models
from django.utils.text import slugify
from parler.models import TranslatableModel, TranslatedFields

# Parent / Əsas kateqoriya
class ParentCategory(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=200, unique=True, verbose_name="Category Name"),
    )
    slug = models.SlugField(max_length=220, unique=True, blank=True)
    image = models.ImageField(upload_to="parent_categories/", blank=True, null=True)

    class Meta:
        verbose_name = "Parent Category"
        verbose_name_plural = "Parent Categories"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.safe_translation_getter("name", any_language=True))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.safe_translation_getter("name", any_language=True)

# Child / Alt kateqoriya
class Category(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=200, unique=True, verbose_name="Category Name"),
        description=models.TextField(blank=True, null=True, verbose_name="Description"),
    )
    slug = models.SlugField(max_length=220, unique=True, blank=True)
    parent = models.ManyToManyField(
        ParentCategory,
        related_name="categories",
    )

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.safe_translation_getter("name", any_language=True))
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.parent} → {self.safe_translation_getter('name', any_language=True)}"



class Products(TranslatableModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    parent_category = models.ForeignKey(ParentCategory, on_delete=models.CASCADE, related_name="products")
    translations = TranslatedFields(
        name=models.CharField(max_length=250, verbose_name="Product Name"),
        description=models.TextField(blank=True, null=True, verbose_name="Description"),
    )
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="products/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ["-created_at"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.safe_translation_getter("name", any_language=True))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.safe_translation_getter("name", any_language=True)

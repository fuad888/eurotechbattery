from django.db import models
from parler.models import TranslatableModel, TranslatedFields
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import slugify


# Create your models here.
class Category(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=200),
        description=RichTextUploadingField(blank=True, null=True)
    )

    def __str__(self):
        # Hal-hazırda aktiv dilə görə name qaytarır
        return self.safe_translation_getter('name', any_language=True)
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

class Brands(models.Model):
    name=models.CharField(max_length=200)
    image=models.ImageField(upload_to='brands/%Y/%m/%d', blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Brand"
        verbose_name_plural = "Brands"

class Product(TranslatableModel):
    Category=models.ManyToManyField(Category, related_name='products')
    Brand=models.ForeignKey(Brands, on_delete=models.CASCADE, related_name='products', null=True, blank=True)
    translations = TranslatedFields(
        name=models.CharField(max_length=200),
        description=RichTextUploadingField(blank=True, null=True)
    )
    price=models.DecimalField(max_digits=10, decimal_places=2)
    stock=models.PositiveIntegerField()
    available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    image=models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    slug=models.SlugField(max_length=200, unique=True, blank=True)

    def __str__(self):
        return self.safe_translation_getter('name', any_language=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.safe_translation_getter('name', any_language=True))
            super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"


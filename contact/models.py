from django.db import models
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields

class contactmessage(models.Model):
    INTEREST_CHOICES = [
        ("products", _("Products")),
        ("services", _("Services")),
        ("support", _("Support")),
        ("other", _("Other")),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    interest = models.CharField(max_length=50, choices=INTEREST_CHOICES)
    message = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.email}"
    

class FAQ(TranslatableModel):
    translations = TranslatedFields(
        question = models.CharField(max_length=255),
        answer = models.TextField()
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.safe_translation_getter('question', any_language=True)

# Create your models here.

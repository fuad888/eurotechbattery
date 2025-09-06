from django.db import models
from django.utils.translation import gettext_lazy as _

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
    



# Create your models here.

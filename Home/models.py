from django.db import models


class Homepage(models.Model):
    image_left = models.ImageField(upload_to='homepage/', blank=True, null=True)
    image_right = models.ImageField(upload_to='homepage/', blank=True, null=True)
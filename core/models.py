from django.db import models

class Setting(models.Model):
    logo = models.ImageField(upload_to='logo/')
    title = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    postal_code = models.CharField(max_length=10)
    address = models.TextField()
    facebook = models.CharField(max_length=100)
    instagram = models.CharField(max_length=100)
    twitter = models.CharField(max_length=100, blank=True, null=True)
    pinterest = models.CharField(max_length=100, blank=True, null=True)
    newsletter = models.CharField(max_length=100, blank=True, null=True)
    newsletter_description = models.TextField(max_length=500, blank=True, null=True)

    def __str__(self):
        return 'Setting'
    
    def has_add_permission(self, request):
        if not request.user.is_staff:
            return False
        return False
    def has_delete_permission(self, request, obj=None):
        if not request.user.is_staff:
            return False
        return False
    
    class Meta:
        verbose_name = 'Setting'
        verbose_name_plural = 'Settings'

# Create your models here.

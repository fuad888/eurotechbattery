from django.db import models

class Setting(models.Model):
    header_logo = models.ImageField(upload_to='logo/',blank=True, null=True)
    fotter_logo = models.ImageField(upload_to='logo/',blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    postal_code = models.CharField(max_length=10, blank=True, null=True)
    address1 = models.TextField(blank=True, null=True)
    address2 = models.TextField(blank=True, null=True)
    facebook = models.CharField(max_length=100, blank=True, null=True)
    instagram = models.CharField(max_length=100, blank=True, null=True)
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

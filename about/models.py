from django.db import models
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields

# Create your models here.
class Aboutpage(TranslatableModel):
    translations = TranslatedFields(
        title = models.CharField(max_length=200, verbose_name=_("Title"))
    )
    hero_photo = models.ImageField(upload_to='about_hero_photos/', verbose_name=_("Hero Photo"))

    class Meta:
        verbose_name = _("About Page")
        verbose_name_plural = _("About Pages")

    def __str__(self):
        return self.safe_translation_getter("title", any_language=True)

class About(TranslatableModel):
    translations = TranslatedFields(
        company_story = models.TextField(verbose_name=_("Company Story")),
        mission = models.TextField(verbose_name=_("Mission")),
        vision = models.TextField(verbose_name=_("Vision")),
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created At"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated At"))

    class Meta:
        verbose_name = _("About")
        verbose_name_plural = _("Abouts")



class team(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(max_length=100, verbose_name=_("Name")),
        position = models.CharField(max_length=100, verbose_name=_("Position")),
    )
    photo = models.ImageField(upload_to='team_photos/', verbose_name=_("Photo"))


    class Meta:
        verbose_name = _("Team Member")
        verbose_name_plural = _("Team Members")

    def __str__(self):
        return self.safe_translation_getter("name", any_language=True)
    
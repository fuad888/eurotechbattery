from django import forms
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from captcha.fields import CaptchaField
from .models import contactmessage


from django import forms
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from captcha.fields import CaptchaField
from .models import contactmessage

class ContactForm(forms.ModelForm):
    captcha = CaptchaField()  # Meta xaricində

    phone = forms.CharField(
        validators=[RegexValidator(
            regex=r'^\+?[0-9]{9,15}$',
            message=_("The phone number must be in the format +994xxxxxxxxx.")
        )],
        widget=forms.TextInput(attrs={"placeholder": _("Phone"), "class": "form-control"})
    )

    class Meta:
        model = contactmessage
        fields = ["name", "email", "phone", "interest", "message"]
        error_messages = {
            'interest': {
                'required': _("Please select an area of ​​interest."),
                'invalid_choice': _("The selected option is incorrect."),
            },
        }
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": _("Name"), "class": "form-control"}),
            "email": forms.EmailInput(attrs={"placeholder": _("Email"), "class": "form-control"}),
            "interest": forms.Select(attrs={"class": "form-control"}),
            "message": forms.Textarea(attrs={"placeholder": _("Message"), "class": "form-control", "rows": 4}),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError("Email is required.")
        return email

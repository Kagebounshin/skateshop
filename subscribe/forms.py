from django import forms
from .models import Subscribe


class SubForm(forms.ModelForm):
    """ For for the user to Subscribe for a Newsletter """
    class Meta:
        model = Subscribe
        fields = ("email_address",)

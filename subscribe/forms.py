from django import forms
from .models import Subcribe


class SubForm(forms.ModelForm):
    """ For for the user to Subscribe for a Newsletter """
    class Meta:
        model = Subcribe
        fields = ("email_address",)

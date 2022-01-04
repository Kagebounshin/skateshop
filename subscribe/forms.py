from django import forms
from .models import Subscribe


class SubscribeNewsForm(forms.ModelForm):
    """ Subscribe User To Newsletter """
    class Meta:
        model = Subscribe
        fields = ('email',)

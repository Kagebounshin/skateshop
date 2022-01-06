from django import forms
from .models import Contact


class UserContactForm(forms.ModelForm):
    """ Form for contact model """
    class Meta:
        model = Contact
        fields = ['full_name', 'email_address',
                  'subject', 'message']

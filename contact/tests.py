from django.test import SimpleTestCase
from contact.forms import UserContactForm

class TestUserContactForm(SimpleTestCase):

    def test_subject_is_required(self):
        form = UserContactForm({'subject': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('subject', form.errors.keys())

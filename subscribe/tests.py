from django.test import SimpleTestCase
from subscribe.forms import SubForm


class TestSubForm(SimpleTestCase):

    def test_subscribe_is_required(self):
        """ Testing required fields """
        form = SubForm({'email': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors.keys())

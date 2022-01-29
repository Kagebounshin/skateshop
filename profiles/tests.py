from django.test import SimpleTestCase
from profiles.forms import UserProfileForm

class TestUserProfileForm(SimpleTestCase):

    def test_no_required_fields(self):
        form = UserProfileForm({'default_phone_number': ''})
        self.assertTrue(form.is_valid())

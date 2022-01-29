from django.test import SimpleTestCase
from django.urls import reverse, resolve
from home.views import index


class TestUrls(SimpleTestCase):

    def test_index_url_resolves(self):
        """ Testing urls for home """
        url = reverse('home')
        self.assertEquals(resolve(url).func, index)

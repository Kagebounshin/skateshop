from django.test import SimpleTestCase
from django.urls import reverse, resolve
from bag.views import view_bag


class TestUrls(SimpleTestCase):

    def test_bag_url_resolves(self):
        """ Testing urls for home """
        url = reverse('view_bag')
        self.assertEquals(resolve(url).func, view_bag)

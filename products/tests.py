from django.test import SimpleTestCase
from django.urls import reverse, resolve
from products.models import Category
from products.views import all_products, add_product


class TestUrls(SimpleTestCase):

    def test_all_products_url_resolves(self):
        """ Testing urls for all_products """
        url = reverse('products')
        self.assertEquals(resolve(url).func, all_products)

    def test_add_products_url_resolves(self):
        """ Testing urls for add_products """
        url = reverse('add_product')
        self.assertEquals(resolve(url).func, add_product)

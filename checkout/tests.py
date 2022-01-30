from django.test import SimpleTestCase
from django.urls import reverse, resolve
from checkout.views import cache_checkout_data, checkout, checkout_success
from checkout.forms import OrderForm


class TestUrls(SimpleTestCase):

    def test_cache_checkout_data_url_resolves(self):
        """ Testing urls for cache_checkout_data """
        url = reverse('cache_checkout_data')
        self.assertEquals(resolve(url).func, cache_checkout_data)

    def test_checkout_url_resolves(self):
        """ Testing urls for checkout """
        url = reverse('checkout')
        self.assertEquals(resolve(url).func, checkout)

    def test_checkout_success_url_resolves(self):
        """ Testing urls for checkout """
        url = reverse('checkout_success', args=['order.order_number'])
        self.assertEquals(resolve(url).func, checkout_success)

class TestOrderForm(SimpleTestCase):

    def test_full_name_is_required(self):
        """ Testing required fields """
        form = OrderForm({'full_name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('full_name', form.errors.keys())

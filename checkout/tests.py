from django.test import TestCase
from django.urls import resolve, reverse
from .views import checkout

# testing for checkout app urls
class TestAccountsUrls(TestCase):
    
    def test_checkout_url(self):
        path = resolve(reverse('checkout'))
        self.assertEqual(path.func, checkout)

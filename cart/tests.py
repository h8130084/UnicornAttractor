from django.test import TestCase
from django.urls import resolve, reverse
from .views import view_cart, add_to_cart, adjust_cart

# testing for cart app urls
class TestAccountsUrls(TestCase):
    
    def test_view_cart_url(self):
        path = resolve(reverse('view_cart'))
        self.assertEqual(path.func, view_cart)

    def test_add_to_cart_url(self):
        path = resolve(reverse('add_to_cart', args=[1]))
        self.assertEqual(path.func, add_to_cart)

    def test_adjust_cart_url(self):
        path = resolve(reverse('adjust_cart', args=[1]))
        self.assertEqual(path.func, adjust_cart)
from django.test import TestCase
from django.urls import resolve, reverse
from .views import logout

# Create your tests here.
class TestAccountsUrls(TestCase):
    
    def test_logout_url(self):
        path = resolve(reverse('logout'))
        self.assertEqual(path.func, logout)
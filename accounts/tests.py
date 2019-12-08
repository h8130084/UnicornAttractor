from django.test import TestCase
from django.urls import resolve, reverse
from .views import logout, login, registration, index, user_profile

# testing for accounts app urls
class TestAccountsUrls(TestCase):
    
    def test_logout_url(self):
        path = resolve(reverse('logout'))
        self.assertEqual(path.func, logout)

    def test_login_url(self):
        path = resolve(reverse('login'))
        self.assertEqual(path.func, login)

    def test_registration_url(self):
        path = resolve(reverse('registration'))
        self.assertEqual(path.func, registration)
        
    def test_index_url(self):
        path = resolve(reverse('index'))
        self.assertEqual(path.func, index)
    
    def test_profile_url(self):
        path = resolve(reverse('profile'))
        self.assertEqual(path.func, user_profile)
    

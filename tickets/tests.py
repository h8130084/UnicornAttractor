from django.test import TestCase
from django.urls import resolve, reverse
from .views import bug, addBug, bugDetails, upvote, edit_bug

# testing for tickets app urls
class TestAccountsUrls(TestCase):
    
    def test_bug_url(self):
        path = resolve(reverse('bug'))
        self.assertEqual(path.func, bug)

    def test_addBugt_url(self):
        path = resolve(reverse('addBug'))
        self.assertEqual(path.func, addBug)

    def test_bugDetails_url(self):
        path = resolve(reverse('bugDetails', args=[1]))
        self.assertEqual(path.func, bugDetails)
        
    def test_upvote_url(self):
        path = resolve(reverse('upvote', args=[1]))
        self.assertEqual(path.func, upvote)
        
    def test_edit_bug_url(self):
        path = resolve(reverse('edit_bug', args=[1]))
        self.assertEqual(path.func, edit_bug)
        
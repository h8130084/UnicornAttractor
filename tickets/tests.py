from django.test import TestCase
from .models import Bug

# Create your tests here.

class BugTests(TestCase):
    """testing"""

    def test_str(self):
        test_name = Bug(name= 'A Bug')
        self.assertEqual(str(test_name), 'A Bug')
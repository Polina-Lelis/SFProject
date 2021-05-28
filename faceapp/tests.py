from django.test import TestCase

from django.test import SimpleTestCase
from django.test import Client

class HomePageViewTestCase(SimpleTestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_request_home_page(self):
        response = self.client.get('/')
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)
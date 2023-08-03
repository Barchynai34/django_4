from django.test import TestCase, Client
from django.urls import reverse


class ExamplesTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_test_view(self):
        response = self.client.get(reverse("test-view"))
        exp_data = "Test"

        self.assertEqual(response.content.decode(), exp_data)
        self.assertEqual(response.status_code, 200)

    def test_test_view_hello(self):
        response = self.client.get(reverse("test-hello"))
        exp_data = "Hello"

        self.assertEqual(response.content.decode(), exp_data)
        self.assertEqual(response.status_code, 500)

    def test_test_view_bye(self):
        response = self.client.get(reverse("test-bye"))
        exp_data = "Goodbye"

        self.assertEqual(response.content.decode(), exp_data)
        self.assertEqual(response.status_code, 200)

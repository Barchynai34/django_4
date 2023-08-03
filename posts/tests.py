
from django.test import TestCase, Client
from django.urls import reverse

class PostsTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index_view(self):
        response = self.client.get(reverse("index-page")) # reverse вернет http://127.0.0.1:8000/
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "posts/index.html")

    def test_contacts_view(self):
        response = self.client.get(reverse("contacts-page"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "posts/contacts.html")
        
    def test_about_view(self):
        response = self.client.get(reverse("about-page"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "posts/about.html")

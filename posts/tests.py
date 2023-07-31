from django.test import TestCase, Client
from django.urls import reverse

from posts.models import Post


class PostsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.post = Post.objects.create(title="Test", content="Test")

    def test_index_view(self):
        response = self.client.get(reverse("index-page"))  # reverse вернет http://127.0.0.1:8000/

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("posts/index.html")

    def test_contacts_view(self):
        response = self.client.get(reverse("contacts-page"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("posts/contacts.html")

    def test_about_view(self):
        response = self.client.get(reverse("about-page"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("posts/about.html")

    def test_post_update(self):
        response = self.client.get(reverse("post-update", args=(self.post.pk,)))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("posts/post_update.html")

    def test_post_delete(self):
        response = self.client.get(reverse("post-delete", args=(self.post.pk,)))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("posts/post_delete.html")
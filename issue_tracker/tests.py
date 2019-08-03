from django.test import TestCase


class ProjectTests(TestCase):

    def test_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_blog_page(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)

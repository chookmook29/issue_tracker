from django.test import TestCase
from blog.models import Blog


class BlogTestCase(TestCase):
    def setUp(self):
        Blog.objects.create(title='test', body='text')

    def test_blog_fields(self):
        """Blog created has its correct default values"""
        blog = Blog.objects.get(title="test")
        self.assertEqual(blog.image, 'default.jpg')
        self.assertEqual(blog.body, 'text')

    def test_blogview_url_exists_at_desired_location(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)

from django.test import TestCase
from blog.models import Blog


class BlogTestCase(TestCase):
    def setUp(self):
        Blog.objects.create(title='test', body='text', id=1)

    def test_blog_fields(self):
        """Blog created has its correct default values"""
        blog = Blog.objects.get(title="test")
        self.assertEqual(blog.image, 'default.jpg')
        self.assertEqual(blog.body, 'text')

    def test_blog_page(self):
        response = self.client.get('/blog/show/1')
        self.assertEqual(response.status_code, 200)

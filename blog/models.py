from django.db import models
from django.conf import settings


class Blog(models.Model):
    author = models.ForeignKey(
             settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default='1')
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField(null=True)
    body = models.TextField()
    image = models.ImageField(upload_to='', default='default.jpg')


class Blog_comment(models.Model):
    ticket = models.ForeignKey(
             'blog.Blog', on_delete=models.CASCADE,
             related_name='blog_comments', default='1')
    author = models.ForeignKey(
             settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    text = models.TextField(verbose_name='Comment text')

    def __str__(self):
        return str(self.ticket) + ' | ' + str(self.pub_date) + ' | ' + str(self.author)

from django.db import models

class Ticket(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()


class Comment(models.Model):
    date = models.DateField(auto_now=True)
    text = models.TextField()

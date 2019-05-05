from django.db import models
from django.conf import settings


class Ticket(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    TO_DO = 'To do'
    DOING = 'Doing'
    DONE = 'Done'
    STATUS_CHOICES = (
        (TO_DO, 'To do'),
        (DOING, 'Doing'),
        (DONE, 'Done'),
    )
    BUG = 'Bug'
    FEATURE = 'Feature'
    TYPE_CHOICES = (
        (BUG, 'Bug'),
        (FEATURE, 'Feature'),
    )
    progress = models.CharField(
               max_length=10, choices=STATUS_CHOICES, default='1')
    ticket_type = models.CharField(
                  max_length=10, choices=TYPE_CHOICES, default='1')


class Comment(models.Model):
    ticket = models.ForeignKey(
             'ticket.Ticket', on_delete=models.CASCADE,
             related_name='comments', default='1')
    author = models.ForeignKey(
             settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    text = models.TextField()

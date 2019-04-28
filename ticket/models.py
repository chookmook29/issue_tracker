from django.db import models


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
    progress = models.CharField(max_length=10, choices=STATUS_CHOICES, default='1')
    ticket_type = models.CharField(max_length=10, choices=TYPE_CHOICES, default='1')


class Comment(models.Model):
    ticket = models.ForeignKey('ticket.Ticket', on_delete=models.CASCADE, related_name='comments', default='1')
    author = models.CharField(default='me', max_length=200)
    date = models.DateField(auto_now=True)
    text = models.TextField()

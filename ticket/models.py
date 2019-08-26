from django.db import models
from django.conf import settings


class Ticket(models.Model):
    title = models.CharField(max_length=50, verbose_name="Title")
    body = models.TextField(verbose_name="Description")
    # Two sets of constants for choice fields, needed for custom fields
    TO_DO = "To do"
    DOING = "Doing"
    DONE = "Done"
    STATUS_CHOICES = ((TO_DO, "To do"), (DOING, "Doing"), (DONE, "Done"))
    BUG = "Bug"
    FEATURE = "Feature"
    TYPE_CHOICES = ((BUG, "Bug"), (FEATURE, "Feature"))
    pub_date = models.DateTimeField(default="2001-01-01")
    progress = models.CharField(max_length=10,
                                choices=STATUS_CHOICES, default="To do")
    # Defaults needed for database migrations, otherwise errors
    upvotes = models.IntegerField(default="0")
    ticket_type = models.CharField(
        max_length=10, choices=TYPE_CHOICES,
        default="1", verbose_name="Ticket type"
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default="1"
    )

    def __str__(self):
        return str(self.title) + " | " + str(self.pub_date)


class Comment(models.Model):
    ticket = models.ForeignKey(
        "ticket.Ticket", on_delete=models.CASCADE,
        related_name="comments", default="1"
    )
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    text = models.TextField(verbose_name="Comment text")

    def __str__(self):
        return str(self.author) + " | " + str(self.date)

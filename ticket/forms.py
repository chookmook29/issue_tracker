from django import forms
from .models import Comment, Ticket


# Comment and ticket forms extended from default class
class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text',)


class TicketForm(forms.ModelForm):

    class Meta:
        model = Ticket
        fields = ('title', 'body', 'ticket_type',)

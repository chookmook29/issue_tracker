from django import forms
from .models import Comment, Ticket


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text',)


class TicketForm(forms.ModelForm):

    class Meta:
        model = Ticket
        fields = ('title', 'body', 'ticket_type',)

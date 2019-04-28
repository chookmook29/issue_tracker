from django.shortcuts import render, redirect, get_object_or_404
from .models import Ticket, Comment
from django.http import HttpResponseRedirect
from .forms import CommentForm


def tickets(request):
    tickets = Ticket.objects.order_by('title')
    comments = Comment.objects.get()
    return render(request, 'ticket/tickets.html', {'tickets': tickets}, {'comments': comments})


def delete(request, ticket_id):
    item = Ticket.objects.get(pk=ticket_id)
    item.delete()
    return redirect('/')


def show(request, ticket_id):
    ticket = Ticket.objects.get(pk=ticket_id)
    return render(request, 'single_ticket.html', {'ticket': ticket})


def add_comment(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.ticket = ticket
            comment.save()
            return redirect('/')
    else:
        form = CommentForm()
    return render(request, 'add_comment.html', {'form': form})

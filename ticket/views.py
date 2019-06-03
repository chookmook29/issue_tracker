from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.utils import timezone
from django.conf import settings
from .models import Ticket, Comment
from .forms import CommentForm, TicketForm


def delete(request, ticket_id):
    item = Ticket.objects.get(pk=ticket_id)
    item.delete()
    return redirect('/')


def show(request, pk):
    if request.method == "POST":
        return redirect('checkout', pk=pk)
    ticket = Ticket.objects.get(pk=pk)
    comment_list = Comment.objects.select_related().filter(
                   ticket_id=pk).order_by('-date')
    paginator = Paginator(comment_list, 4)
    page = request.GET.get('page')
    comments = paginator.get_page(page)
    key = settings.STRIPE_PUBLISHABLE_KEY
    return render(request, 'single_ticket.html', {'ticket': ticket, 'comments':
                  comments, 'key': key})


def add_comment(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.ticket = ticket
            comment.author = request.user
            comment.save()
            return redirect('show_single', pk=pk)
    else:
        form = CommentForm()
    return render(request, 'add_comment.html', {'form': form})


def add_ticket(request):
    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.progress = 'To do'
            ticket.author = request.user
            ticket.pub_date = timezone.now()
            ticket.save()
            return redirect('home')
    else:
        form = TicketForm()
    return render(request, 'new_ticket.html', {'form': form})

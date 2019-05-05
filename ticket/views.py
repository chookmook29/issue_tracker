from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .models import Ticket, Comment
from .forms import CommentForm


def tickets(request):
    tickets = Ticket.objects.order_by('title')
    return render(request, 'ticket/tickets.html', {'tickets': tickets})


def delete(request, ticket_id):
    item = Ticket.objects.get(pk=ticket_id)
    item.delete()
    return redirect('/')


def show(request, pk):
    ticket = Ticket.objects.get(pk=pk)
    comment_list = Comment.objects.select_related().filter(
                   ticket_id=pk).order_by('-date')
    paginator = Paginator(comment_list, 4)
    page = request.GET.get('page')
    comments = paginator.get_page(page)
    return render(request, 'single_ticket.html', {'ticket': ticket, 'comments':
                  comments})


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

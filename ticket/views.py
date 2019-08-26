from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.utils import timezone
from django.conf import settings
from django.contrib import messages
from django.db.models import Count
from .models import Ticket, Comment
from .forms import CommentForm, TicketForm
from users.models import CustomUser


def delete(request, ticket_id):
    item = Ticket.objects.get(pk=ticket_id)
    item.delete()
    # messages from django.contrib improve UX
    messages.success(request, ("Ticket deleted!"))
    return redirect("/")


def show(request, pk):
    if request.method == "POST":
        return redirect("checkout", pk=pk)
    ticket = Ticket.objects.get(pk=pk)
    # comments paginated with paginator module for simplicity
    comment_list = (
        Comment.objects.select_related().filter(ticket_id=pk).order_by("-date")
    )
    paginator = Paginator(comment_list, 4)
    page = request.GET.get("page")
    comments = paginator.get_page(page)
    # Environmental variable for safety
    key = settings.STRIPE_PUBLISHABLE_KEY
    return render(
        request,
        "single_ticket.html",
        {"ticket": ticket, "comments": comments, "key": key},
    )


def add_comment(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        # Standard attributes and methods when posting
        if form.is_valid():
            comment = form.save(commit=False)
            comment.ticket = ticket
            comment.author = request.user
            comment.save()
            user = CustomUser.objects.get(username=request.user)
            # Comments amount needs counting to measure user activity
            user.amount_comments += 1
            user.save()
            messages.success(request, ("Comment added!"))
            return redirect("show_single", pk=pk)
    else:
        form = CommentForm()
    return render(request, "add_comment.html", {"form": form})


def add_ticket(request):
    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.progress = "To do"
            ticket.author = request.user
            ticket.pub_date = timezone.now()
            ticket.save()
            messages.success(request, ("Ticket added!"))
            return redirect("home")
    else:
        form = TicketForm()
    return render(request, "new_ticket.html", {"form": form})


def all_tickets(request):
    """ Reverse order to make most upvoted ticket appear on top"""
    all_tickets = Ticket.objects.order_by("pub_date").reverse()
    return render(request, "all_tickets.html", {"all_tickets": all_tickets})


def all_upvotes(request):
    all_tickets = Ticket.objects.order_by("upvotes").reverse()
    return render(request, "all_tickets.html", {"all_tickets": all_tickets})


def all_commented(request):
    all_tickets = Ticket.objects.annotate(num_comments=Count("comments")).order_by(
        "-num_comments"
    )
    return render(request, "all_tickets.html", {"all_tickets": all_tickets})


def all_feature(request):
    all_tickets = Ticket.objects.filter(ticket_type="Feature")
    return render(request, "all_tickets.html", {"all_tickets": all_tickets})


def all_bug(request):
    all_tickets = Ticket.objects.filter(ticket_type="Bug")
    return render(request, "all_tickets.html", {"all_tickets": all_tickets})

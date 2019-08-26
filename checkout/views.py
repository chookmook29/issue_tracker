from django.shortcuts import render
from ticket.models import Ticket
from users.models import CustomUser
from django.contrib import messages


def checkout(request, pk):
    ticket = Ticket.objects.get(pk=pk)
    user = CustomUser.objects.get(username=request.user)
    user.contributions += 5
    user.save()
    ticket.upvotes += 1
    ticket.save()
    # messages from django.contrib improve UX
    messages.success(request, ("Thank you for your payment!"))
    return render(request, "checkout.html", {"ticket": ticket})

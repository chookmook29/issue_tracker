from django.shortcuts import render
from ticket.models import Ticket
from users.models import CustomUser


def checkout(request, pk):
    ticket = Ticket.objects.get(pk=pk)
    user = CustomUser.objects.get(username=request.user)
    user.contributions += 5
    user.save()
    ticket.upvotes += 1
    ticket.save()
    return render(request, 'checkout.html', {'ticket': ticket})

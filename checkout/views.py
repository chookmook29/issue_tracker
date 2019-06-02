from django.shortcuts import render
from ticket.models import Ticket


def checkout(request, pk):
    ticket = Ticket.objects.get(pk=pk)
    return render(request, 'checkout.html', {'ticket': ticket})

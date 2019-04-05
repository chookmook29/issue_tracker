from django.shortcuts import render
from .models import Ticket

def tickets(request):
	tickets = Ticket.objects.order_by('title')
	return render(request, 'ticket/tickets.html', {'tickets': tickets})

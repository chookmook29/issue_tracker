from django.shortcuts import render, redirect
from .models import Ticket
from django.http import HttpResponseRedirect

def tickets(request):
	tickets = Ticket.objects.order_by('title')
	return render(request, 'ticket/tickets.html', {'tickets': tickets})

def delete(request, ticket_id):
	item = Ticket.objects.get(pk=ticket_id)
	item.delete()
	return redirect('/')
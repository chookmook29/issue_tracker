from django.shortcuts import render

def tickets(request):
	return render(request, 'ticket/tickets.html')

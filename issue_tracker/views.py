from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from ticket.models import Ticket


def home(request):
    return render(request, 'index.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('login')
    else:
        return render(request, 'login.html')


def sign_up(request):
    return render(request, 'sign_up.html')


def logout_user(request):
    logout(request)
    return redirect('home')


def all_tickets(request):
    all_tickets = Ticket.objects.order_by('upvotes').reverse()
    return render(request, 'all_tickets.html', {'all_tickets': all_tickets})

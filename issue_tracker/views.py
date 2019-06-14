from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
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
            messages.success(request, ('User logged in!'))
            return redirect('home')
        else:
            messages.success(request, ('Error please try again!'))
            return redirect('login')
    else:
        return render(request, 'login.html')


def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ('You successfully signed up!'))
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'sign_up.html', {'form': form})


def logout_user(request):
    logout(request)
    messages.success(request, ('User logged out!'))
    return redirect('home')


def all_tickets(request):
    all_tickets = Ticket.objects.order_by('upvotes').reverse()
    return render(request, 'all_tickets.html', {'all_tickets': all_tickets})

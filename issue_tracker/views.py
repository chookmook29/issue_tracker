from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


def home(request):
	return render(request, 'index.html')


def blog(request):
	return render(request, 'blog.html')


def ticket(request):
	return render(request, 'ticket.html')


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
		return render(request, 'login.html')\

def logout_user(request):
	logout(request)
	return redirect('home')
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout

def home(request):
	return render(request, 'index.html')


def blog(request):
	return render(request, 'blog.html')


def ticket(request):
	return render(request, 'ticket.html')


def login_user(request):
	return render(request, 'login.html')
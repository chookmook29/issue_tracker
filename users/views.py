from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from users.forms import CustomUserCreationForm, CustomUserChangeForm
from users.models import CustomUser


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # messages from django.contrib improve UX
            messages.success(request, ('User logged in!'))
            return redirect('home')
        else:
            messages.success(request, ('Error please try again!'))
            return redirect('login')
    else:
        return render(request, 'login.html')


def sign_up(request):
    if request.method == 'POST':
        # CustomUserCreationForm necessary if CustomUser's being used
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # cleaned_data attribute necessary for is_valid() method
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ('You successfully signed up!'))
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'sign_up.html', {'form': form})


def logout_user(request):
    # Simple logout using django.contrib.auth module
    logout(request)
    messages.success(request, ('User logged out!'))
    return redirect('home')


def change_details(request):
    if request.method == 'POST':
        # CustomUserCreationForm necessary if CustomUser's being used
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            # cleaned_data attribute necessary for is_valid() method
            email = form.cleaned_data['email']
            user = authenticate(email=email)
            login(request, user)
            messages.success(request,
                             ('You successfully changed your details!'))
            return redirect('home')
    else:
        form = CustomUserChangeForm(instance=request.user)
    user_account = CustomUser.objects.get(username=request.user)
    return render(request, 'change.html',
                  {'form': form, 'user_account': user_account})

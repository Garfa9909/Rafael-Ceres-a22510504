from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm, LoginForm

def register_view(request):
    form = RegisterForm(request.POST)
    if(form.is_valid()):
        form.save()
        return redirect("login")
    context = {'form':form}
    return render(request, 'accounts/register.html', context)

def login_view(request):
    form = LoginForm(request.POST)

    if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('index')

    context = {'form':form}
    return render(request, 'accounts/login.html', context)

def logout_view(request):
    logout(request)
    return redirect('login')


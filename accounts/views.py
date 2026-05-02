from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm, LoginForm, MagicLinkLoginForm
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.models import Group


def register_view(request):
    form = RegisterForm(request.POST)
    if(form.is_valid()):
        user = form.save()
        group = Group.objects.get(name='autores')
        user.groups.add(group)
        login(request, user)
        return redirect("index")
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
            else:   
                context = {'form':form, 'valid':False}
                return render(request, 'accounts/login.html', context)


    context = {'form':form, 'valid':True}
    return render(request, 'accounts/login.html', context)

def logout_view(request):
    logout(request)
    return redirect('login')

def magic_link_login_request_view(request):
    form = MagicLinkLoginForm(request.POST)
    if form.is_valid():
        email = form.cleaned_data['email']

        if(User.objects.filter(email=email).exists()):
            user = User.objects.get(email=email)
            uid = urlsafe_base64_encode(force_bytes(user.pk))

            token = default_token_generator.make_token(user)

            link = request.build_absolute_uri(reverse('magic-link-login', args=[uid, token])
)

            send_mail(
                "Magic Link Login",
                f"Click here to log in: {link}",
                "gestor@portfolio.pt", 
                [email],
            )
            print(link)

            return redirect("index")
        else:
            context = {'form':form, 'valid':False}
            return render(request, 'accounts/magic_link_login.html', context)
    else:
        context = {'form':form, 'valid':True}
        return render(request, 'accounts/magic_link_login.html', context)


def magic_link_login_view(request, uidb64, token):
    uid = force_str(urlsafe_base64_decode(uidb64))
    user = User.objects.get(pk=uid)
    print(user)

    if default_token_generator.check_token(user, token):
        login(request, user)
        return redirect('index')
    else:
        return redirect('login')

    

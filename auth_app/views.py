from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.template.context_processors import csrf

from auth_app.forms.forms import RegisterForm

# Create your views here.


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'reg_form': RegisterForm(),
    }
    return render(request, 'auth_app/register.html', context)


def log_in(request):
    args = {}
    args.update(csrf(request))
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            args['login_error'] = 'Пользователь не найден'
            return render(request, 'auth_app/login.html', args)
    else:
        return render(request, 'auth_app/login.html', args)


def log_out(request):
    logout(request)
    return redirect('home')
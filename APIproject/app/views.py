from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm

from .forms import UserRegisterForm, UserLoginForm
from django.contrib.auth import login, logout

# Create your views here.
def home(request):
    context = {
        'title': 'Главная страница'
    }

    return render(request, 'app/index.html', context=context)

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Регистрация прошла успешна')
            user = form.save()
            login(request, user)
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()

    context = {
        'form': form,
        'title': 'Регистрация'
    }

    return render(request, 'app/register.html', context=context)

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('Home')
    else:
        form = UserLoginForm

    context = {
        'form': form,
        'title': 'Авторизация'
    }

    return render(request, 'app/login.html', context=context)

def user_logout(request):
    logout(request)
    return redirect('Login')

def profile(request):
    return render(request, 'app/profile.html')

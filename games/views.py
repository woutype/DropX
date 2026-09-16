from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def register(request):
    if request.method == 'POST':
        nickname = request.POST.get('nickname', '').strip()
        password = request.POST.get('password', '').strip()

        if not nickname or not password:
            return render(request, 'index.html', {
                'error': 'Пожалуйста, заполните все поля'
            })

        if User.objects.filter(username=nickname).exists():
            user = authenticate(request, username=nickname, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')
            else:
                return render(request, 'index.html', {'error': 'Неверный пароль, попробуй еще раз'})
        else:
            user = User.objects.create_user(username=nickname, password=password)
            login(request, user)
            return redirect('profile')

    return render(request, 'index.html')

def profile(request):
    return render(request, 'pages/profile.html')

def upgrade(request):
    return render(request, "pages/upgrade.html")

def plus(request):
    return render(request, 'pages/plus.html')

def battery(request):
    return render(request, 'pages/battery.html')

def out(request):
    logout(request)
    return redirect('registration')
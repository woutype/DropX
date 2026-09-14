from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

def register(request):
    error = None

    if request.method == 'POST':
        nickname = request.POST.get('nickname', '').strip()
        password = request.POST.get('password', '')

        if User.objects.filter(username=nickname).exists():
            user = authenticate(request, username=nickname, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')
            else:
                error = "Неверный пароль!"
        else:
            user = User.objects.create_user(username=nickname, password=password)
            login(request, user)
            return redirect('profile')

    return render(request, 'index.html', {'error': error})


def profile(request):
    return render(request, 'pages/profile.html')
from django.shortcuts import render
from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        nickname = request.POST.get('nickname')
        password = request.POST.get('password')

        if User.objects.filter(username=nickname).exists():
            print(f"Ошибка: ник {nickname} уже занят!")
        else:
            user = User.objects.create_user(username=nickname, password=password)
            print(f"Успех! Игрок {user.username} записан в Postgres (ID: {user.id})")

    return render(request, 'index.html')

def main_page(request):
    return render(request, 'pages/main.html')
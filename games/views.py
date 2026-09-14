from django.shortcuts import render

def register(request):
    if request.method == 'POST':
        nickname = request.POST.get('nickname')
        password = request.POST.get('password')
        print(f"Пришли данные -> Имя: {nickname} | Пароль: {password}")

    return render(request, 'index.html')
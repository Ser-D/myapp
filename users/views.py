from django.shortcuts import render

def login(request):
    context = {
        'title': 'Home - Авторизація'
    }
    return render(request, 'user/login.html', context)


def registration(request):
    context = {
        'title': 'Home - Реєстрація'
    }
    return render(request, 'user/registration.html', context)


def profile(request):
    context = {
        'title': 'Home - Кабінет'
    }
    return render(request, 'user/profile.html', context)


def logout(request):
    ...
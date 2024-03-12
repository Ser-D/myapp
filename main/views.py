from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context: dict[str, str] = {
        'title': 'Home - Головна',
        'content': 'Магазин меблів HOME',
    }
    return render(request, 'main/index.html', context)


def about(request):
    context: dict[str, str] = {
        'title': 'Home - Про нас',
        'content': 'Про нас',
        'text_on_page': 'Класний магазин, якісний товар та крутий Я!!! )))'
    }
    return render(request, 'main/about.html', context)

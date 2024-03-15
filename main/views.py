from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories


def index(request):

    categories = Categories.objects.all()

    context: dict[str, str] = {
        'title': 'Home - Головна',
        'content': 'Магазин меблів HOME',
        'categories': categories
    }
    return render(request, 'main/index.html', context)


def about(request):
    context: dict[str, str] = {
        'title': 'Home - Про нас',
        'content': 'Про нас',
        'text_on_page': 'Класний магазин, якісний товар та крутий Я!!! )))'
    }
    return render(request, 'main/about.html', context)

from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from goods.models import Products


def catalog(request, category_slug, page=1):

    if category_slug == 'all':
        goods = Products.objects.all()
    else:
        goods: Products = get_object_or_404(Products.objects.filter(category__slug=category_slug))

    paginator = Paginator(goods, 3)
    current_page = paginator.page(page)

    context: dict[str, str] = {
        "title": "Home - Каталог",
        "content": "Про нас",
        "goods": current_page, 
           
    }
    return render(request, "goods/catalog.html", context)


def product(request, product_slug):

    product: Products = Products.objects.get(slug=product_slug)

    context: dict[str, str] = {
        "product": product
    }
    return render(request, "goods/product.html", context=context)

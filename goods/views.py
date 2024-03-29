from django.shortcuts import render

from goods.models import Products


def catalog(request):

    goods = Products.objects.all()

    context: dict[str, str] = {
        "title": "Home - Каталог",
        "content": "Про нас",
        "goods": goods, 
           
    }
    return render(request, "goods/catalog.html", context)


def product(request, product_slug):

    product: Products = Products.objects.get(slug=product_slug)

    context: dict[str, str] = {
        "product": product
    }
    return render(request, "goods/product.html", context=context)

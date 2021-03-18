from django.shortcuts import render, get_object_or_404
import json
from django.conf import settings
from datetime import datetime
from .models import Product, ProductCategory, Locations

# Create your views here.


def index(request):
    title = "магазин"
    product = Product
    content = {
        "title": title,
        "product": product
    }

    return render(request, 'mainapp/index.html', content)


def products(request, pk=None):
    title = "товары"
    links_menu = ProductCategory.objects.all()
    '''links_menu = [
        {"href":"products_all", "name": "все"},
        {"href":"products_home", "name": "дом"},
        {"href":"products_office", "name": "офис"},
        {"href":"products_modern", "name": "модерн"},
        {"href":"products_classic", "name": "классика"}
    ]'''
    quantity = 0
    price = 0
    if request.user.is_authenticated:
        basket = request.user.basket.all()
        if basket:
            quantity = basket[0].total_quantity
            price = basket[0].total_price

    else:
        basket = []

    if pk is None or pk == 0:
        same_products = Product.objects.all()[:3]
    else:
        same_products = Product.objects.filter(category=pk)


    ''' for prod in basket:
        quantity += prod.quantity'''

    print(quantity)

    content = {
        "title": title,
        "links_menu": links_menu,
        "same_products": same_products,
        "media_url": settings.MEDIA_URL,
        "basket": basket,
        "quantity": quantity,
        "price": price
    }
    return render(request, 'mainapp/products.html', content)


def product(request, pk):
    title = "информация о товаре"
    product = get_object_or_404(Product, pk=pk)
    basket = request.user.basket.all()
    content = {
        "title": title,
        "links_menu": ProductCategory.objects.all(),
        "product": product,
        "basket": basket,
        "media_url": settings.MEDIA_URL,
    }
    return render(request, "mainapp/product.html", content)


def contact(request):
    title = "о нас"
    date = datetime.now()
    print(date)
    content = {
        "title": title,
        "locations": Locations.objects.all(),
        "date": date
    }

    return render(request, 'mainapp/contact.html', content)

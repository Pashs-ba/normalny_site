from django.shortcuts import render
from .models import *


def all_products_page(request):
    products = Product.objects.all()
    for i in products:
        print(i.images_list)
    return render(request, 'all_products.html', {
        'products': Product.objects.all()
    })


def en_all_products_page(request):
    products = Product.objects.all()
    for i in products:
        print(i.images_list)
    return render(request, 'all_products.html', {
        'products': Product.objects.all()
    })


def product(request, pk):

    return render(request, 'product.html', {
        'product': Product.objects.get(pk=pk)
    })


def en_product(request, pk):

    return render(request, 'en_product.html', {
        'product': Product.objects.get(pk=pk)
    })

from django.shortcuts import render
from products.models import Product
from django.http import JsonResponse

def products_list(request):
    products = Product.objects.all()
    data = {
        'products': list(products.values_list()),
    }

    return JsonResponse(data)

def products_details(request, pk):
    product = Product.objects.get(pk=pk)
    data = {
        'name': product.name,
        'description': product.description,
        'active': product.active,
    }
    return JsonResponse(data)

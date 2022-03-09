from django.shortcuts import render
from products.models import Product
from django.http import JsonResponse

from django.http import HttpResponse
from .resources import CategoryResource

from tablib import Dataset


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


def export(request):
    category_resource = CategoryResource()
    dataset = category_resource.export()
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="categories.csv"'
    return response


def simple_upload(request):
    if request.method == 'POST':
        category_resource = CategoryResource()
        dataset = Dataset()
        new_categories = request.FILES['myfile']

        imported_data = dataset.load(new_categories.read())
        result = category_resource.import_data(dataset, dry_run=True)  # Test the data import

        if not result.has_errors():
            category_resource.import_data(dataset, dry_run=False)  # Actually import now

    return render(request, 'products/import.html')

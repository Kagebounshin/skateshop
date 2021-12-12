from django.shortcuts import render
from .models import Products

# Create your views here.

def all_products(request):
    """ A View to show all the products, including sorting and searching """

    products = Products.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)

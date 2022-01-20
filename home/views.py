from django.shortcuts import render
from products.models import Product


def index(request):
    """ View for index page """
    products = Product.objects.all()

    context = {
        'products': products
    }
    return render(request, 'home/index.html', context)

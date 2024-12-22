from django.shortcuts import render
from django.views.generic import (
ListView)

from .models import Product

# Create your views here.
def shop(request):
    """ Index page view """

    return render(request, 'shop/shop.html')
class Product(ListView):
    """List of products view"""
    template_name = "shop/shop.html"
    model = Product
    context_object_name = 'products'
    paginate_by = 4

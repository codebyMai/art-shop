from django.shortcuts import render
from .models import Product
from django.views.generic import (ListView, DetailView)

class Shop(ListView):
    """Main Shop page"""
    template_name = "products/shop.html"
    model = Product
    context_object_name = 'products'
    
class Products(ListView):
    """List of products view"""
    template_name = "products/products.html"
    model = Product
    context_object_name = 'products'

class ProductDetail(DetailView):
    """Detailed product view"""
    model = Product
    template_name = 'products/detail.html'

def faq(request):
    """FAQ page view """
    return render(request, 'products/faq.html')    


    

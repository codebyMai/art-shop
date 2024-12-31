from django.shortcuts import render
from .models import Product
from django.views.generic import (ListView, DetailView)

class Shop(ListView):
    """Main Shop page"""
    template_name = "products/shop.html"
    model = Product
    context_object_name = 'products'
    paginate_by = 4

def miniature(request):
    products = Product.objects.filter(is_miniature=True).values()

def featured(request):
    products = Product.objects.filter(is_miniature=False).values()    
  
class Products(ListView):
    """List of products view"""
    template_name = "products/products.html"
    model = Product
    context_object_name = 'products'
    

class ProductDetail(DetailView):
    """Detailed product view"""
    model = Product
    template_name = 'products/detail.html'


    

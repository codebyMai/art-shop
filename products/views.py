from django.shortcuts import render
from .models import Product
from django.views.generic import (ListView, DetailView)

class Shop(ListView):
    """Main Shop page"""
    template_name = "products/shop.html"
    model = Product
    context_object_name = 'products'
    paginate_by = 4

def painting(request):
    products = Product.objects.filter(is_miniature=False)   
  

class Products(ListView):
    """List of products view"""
    template_name = "products/products.html"
    model = Product
    context_object_name = 'products'

class ProductDetail(DetailView):
    """Detailed product view"""
    model = Product
    template_name = 'products/detail.html'

class Miniature(ListView):
    products = Product.objects.filter(is_miniature=True)     
    template_name= "products/products.html"
    model = Product
    context_object_name = 'miniature'

class Painting(ListView):
    products = Product.objects.filter(is_miniature=False)     
    template_name= "products/products.html"
    model = Product
    context_object_name = 'painting'    

    

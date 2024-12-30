from django.shortcuts import render
from .models import Product
from django.views.generic import (
ListView, DetailView)


#def shop(request):
   # """ Shop page view """
    #return render(request,'shop.html')

class Shop(ListView):
    """List of quotes view"""
    template_name = "products/shop.html"
    model = Product
    context_object_name = 'products'
    paginate_by = 4

#def products(request):
   #return render(request, 'shop/products.html')

class Products(ListView):
    """List of products view"""
    template_name = "products/products.html"
    model = Product
    context_object_name = 'products'
    



    

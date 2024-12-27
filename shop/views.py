from django.shortcuts import render
from django.views.generic import (
ListView, DetailView)

from .models import Product

# Create your views here.
def shop(request):
    """ Main shop page view """
    return render(request, 'shop/shop_base.html')

#def products(request):
    #image = Products.objects.all().order_by('-posted_date')
   # return render(request, 'shop/products.html')
      

class Products(ListView):
    """List of products view"""
    template_name = "shop/products.html"
    model = Product
    context_object_name = 'products'
    paginate_by = 4
  

class ProductDetail(DetailView):
    """Detailed product view"""
    model = Product
    template_name = 'product_detail.html'
 

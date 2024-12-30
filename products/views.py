from django.shortcuts import render
from .models import Product

def shop(request):
    """ Shop page view """

    return render(request,'products/shop.html')



    

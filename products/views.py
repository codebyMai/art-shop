from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Product
from .forms import ProductForm
from django.contrib import messages
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

def add_product(request):
    """ Add a product to the store """
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()
        
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

def edit_product(request, product_id):
    """ Edit a product in the store """
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.title}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)    
    
def delete_product(request, product_id):
    """ Delete a product from the store """
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))



    

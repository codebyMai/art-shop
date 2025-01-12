from django.shortcuts import render
from .models import Painting
from django.views.generic import ListView

# Create your views here.
class Gallery(ListView):
    """Gallery page"""
    template_name = "gallery/paintings.html"
    model = Painting
    context_object_name = 'gallery'
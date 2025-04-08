from django.shortcuts import render
from .models import Painting
from django.views.generic import ListView


class Gallery(ListView):
    """Gallery page view"""
    template_name = "gallery/paintings.html"
    model = Painting
    context_object_name = 'gallery'

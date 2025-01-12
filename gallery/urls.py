from django.urls import path
from . import views
from .views import Gallery

urlpatterns = [
    path('', Gallery.as_view(), name='gallery'),
]

from django.urls import path
from . import views
from .views import Products, Shop

urlpatterns = [

    path('shop/', Shop.as_view(), name='shop'),
    path('', Products.as_view(), name='products'),
]

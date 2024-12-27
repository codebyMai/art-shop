from django.urls import path
from . import views
from .views import Products, ProductDetail

urlpatterns = [
    path('', views.shop, name='shop'),
    path('products/', Products.as_view(), name='products'),
    #path('product/<int:id>/', ProductDetail.as_view(),name='product-detail'),
    path('products/<int:pk>/', ProductDetail.as_view(), name='product-detail')
]

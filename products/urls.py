from django.urls import path
from . import views
from .views import Products, Shop, ProductDetail

urlpatterns = [

    path('shop/', Shop.as_view(), name='shop'),
    path('', Products.as_view(), name='products'),
    path('product/<int:pk>/', ProductDetail.as_view(), name='detail'),
    path('faq/', views.faq, name='faq'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
]

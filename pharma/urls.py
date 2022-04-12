from django.urls import path
from . import views

app_name = 'pharma'

urlpatterns = [
    path('', views.billing, name='billing'),
    path('purchase', views.purchase, name='purchase'),
    path('products', views.view_products, name='products'),
    path('addmedicine', views.addmedicine, name='addmedicine'),
    path('addpharmacyst', views.add_pharmacyst, name='addpharmacyst'),
    path('price',views.price_show, name='price'),
    path('total',views.total, name='total'),
    path('checkout',views.checkout, name='checkout'),


  
]
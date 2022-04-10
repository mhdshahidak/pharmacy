from django.urls import path
from . import views

app_name = 'pharma'

urlpatterns = [
    path('', views.home, name='home'),
    path('purchase', views.purchase, name='purchase'),
    path('products', views.view_products, name='products'),
    path('addmedicine', views.addmedicine, name='addmedicine'),
    path('addpharmacyst', views.add_pharmacyst, name='addpharmacyst'),
    path('bill', views.billing, name='bill'),

  
]
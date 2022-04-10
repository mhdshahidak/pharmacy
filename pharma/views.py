from django.shortcuts import render

from pharma.models import Medicine

# Create your views here.
def home(request):
    return render(request,'home.html')

def addmedicine(request):
    msg = ""
    if request.method == 'POST':
        
        med_name = request.POST['name']
        qty = request.POST['qty']
        p_cost = request.POST['pcost']
        s_cost = request.POST['scost']

        new_med = Medicine(name=med_name,quantity=qty,puchase_cost=p_cost,selling_cost=s_cost)
        new_med.save()
        msg = "Medicine added successfully"

    return render(request,'addmed.html', {'msg':msg,})

def purchase(request):
    return render(request,'purchase.html')

def view_products(request):
    return render(request,'allproducts.html')

def add_pharmacyst(request):
    return render(request,'addpharmacyst.html')

def billing(request):
    return render(request,'bill.html')
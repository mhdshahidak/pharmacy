from tokenize import Number
from unicodedata import name
from django.shortcuts import redirect, render
from django.http import JsonResponse


from pharma.models import Medicine

# Create your views here.
# def home(request):
#     return render(request,'home.html')

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

    medicine = Medicine.objects.filter(quantity__lte=10)  #filter where quantity lessthan 10
    
    return render(request,'purchase.html',{'medicine':medicine,})

def view_products(request):
    medicine = Medicine.objects.all()
    return render(request,'allproducts.html',{'medicine':medicine,})

def add_pharmacyst(request):
    return render(request,'addpharmacyst.html')

def billing(request):
    medicine = Medicine.objects.all()

    if request.method == 'POST':
        mid = request.POST['medicine']
        qty = request.POST['qty']
        medicineqty = Medicine.objects.get(id=mid)

        medicineqty.quantity = medicineqty.quantity - int(qty)
        medicineqty.save()
        return render(request,'bill.html',{'medicine':medicine,})

        
    return render(request,'bill.html',{'medicine':medicine,})


def price_show(request):
    id = request.GET['id']
    # print(id)
    try:
        price = Medicine.objects.get(id=id)
        return render(request,'price.html',{'price':price.selling_cost})
    except:
        return render(request,'price.html',{'price':0})

def total(request):
    price = request.GET['price']
    qty = request.GET['qty']
    try:
        total_price = int(qty) * int(price)
        gst = (total_price * 5)/100
        grand_total = int(total_price+gst)
        # print(total_price)
        # print(gst)
        # print(grand_total)
        return render(request,'total.html',{'total_price':total_price,})
    except:
        return render(request,'total.html',{'total_price':0})


def gst(request):
    
    med = request.GET['id']
    qty = request.GET['qty']

    medid = Medicine.objects.get(id=med)
    cost = medid.selling_cost
    total = int(cost) * int(qty)
    gst = (total * 5)/100
    print(gst)

    return render(request,'gst.html',{'gst':gst,})

def grandtotal(request):
    
    med = request.GET['id']
    qty = request.GET['qty']

    medid = Medicine.objects.get(id=med)
    cost = medid.selling_cost
    total = int(cost) * int(qty)
    gst = (total * 5)/100
    gtotal = total + gst

    return render(request,'gtotal.html',{'gtotal':gtotal,})


    
# def checkout(request):
#     pass
    
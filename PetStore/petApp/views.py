from django.shortcuts import render, HttpResponseRedirect
from .models import Product, Cart
from .forms import ProductForm
from django.contrib import messages
from django.db.models import Q

# Create your views here.

def Index(request):
    if request.method == "POST":
        fm = ProductForm(request.POST,request.FILES)
        print(fm)
        if fm.is_valid():
            fm.save()
            fm = ProductForm()
            return HttpResponseRedirect('/display/')
    else:
        fm = ProductForm()
    return render(request,'index.html',{'form':fm})

def Display(request):
    data = Product.objects.all()
    print(data)
    return render(request,'display.html',{'data':data})

def Delete(request,id):
    if request.method == "POST":
        ## print(id)
        os = Product.objects.get(pk=id)
        os.delete()
        messages.success(request,"Data Deleted Succeessfully")
        return HttpResponseRedirect('/display/')

def Update(request,id):
    if request.method == "POST":
        os = Product.objects.get(pk=id)
        fm = ProductForm(request.POST, request.FILES, instance=os)
        if fm.is_valid():
            fm.save()
            messages.success(request,"Data Updated Succesfully")
            return HttpResponseRedirect('/display/')
    else:
        os = Product.objects.get(pk=id)
        # print(os)
        fm = ProductForm(instance=os)
    return render(request, 'update.html',{'Updateform':fm})

def UserBase(request):
    return render(request,'user/base.html')

def UserIndex(request):
    data = Product.objects.all()
    return render(request,'user/index.html',{'data':data})

def AddToCart(request):
    if request.method == "POST":
        cid = request.POST.get('cid')
        Cart.objects.create(product_id=cid)
    cid = Cart.objects.all().values_list('product_id',flat=True)
    cartdata = Product.objects.filter(id__in=cid)
    amount = Product.objects.filter(id__in=cid).values_list('price',flat=True)
    amt=0
    for i in amount:
        amt=amt+i
    return render(request,'user/cart.html',{'cdata':cartdata,'amt':amt})

def RemoveCart(request,id):
    if request.method == "POST":
        Cart.objects.filter(product_id=id).delete()
        return HttpResponseRedirect('/cart/')
    
def ComponetSearch(request):
    try:
        if request.method == "POST":
            search = request.POST.get('search')

            sdata = Product.objects.filter(Q(category=search) | Q(pname=search) | Q(desc__contains=search) |Q(price__contains=search))
                                            
            print(sdata)
        return render(request, 'user/search.html',{'sdata':sdata})
    except:
        return HttpResponseRedirect('/userindex/')
    
def Details(request,id):
    data_detail = Product.objects.filter(pk=id)
    print(data_detail)
    return render(request,'user/details.html',{'data':data_detail})
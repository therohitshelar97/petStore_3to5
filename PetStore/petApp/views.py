from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from .models import Product, Cart, Address
from .forms import ProductForm
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail 
from django.conf import settings
# Create your views here.

def Email(request):
    send_mail('Welcome', 'Nothing Special.......',settings.EMAIL_HOST_USER,['prasadmhasal@gmail.com','omsawant2525@gmail.com'])
    return HttpResponse('Mail Sending.....')

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
    if request.user.is_authenticated:
        count = Cart.objects.all().count()
        # print(count)
        return render(request,'user/base.html',{'count':count})
    else:
        return HttpResponseRedirect('/')

def UserIndex(request):
    if request.user.is_authenticated:
        data = Product.objects.all()
        count = Cart.objects.filter(user_id=request.user).count()
        return render(request,'user/index.html',{'data':data,'count':count})
    else:
        return HttpResponseRedirect('/')

def AddToCart(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            cid = request.POST.get('cid')
            filter1 = Cart.objects.filter(user_id=request.user).values_list('product_id',flat=True)
            # print(type(cid))
            if int(cid) not in filter1: 
                Cart.objects.create(product_id=cid,user=request.user)
                return HttpResponseRedirect('/cart/')
            else:
                messages.success(request,"This Product Is Alredy Added In Cart")
        cid = Cart.objects.filter(user_id=request.user).values_list('product_id',flat=True)
        cartdata = Product.objects.filter(id__in=cid)
        amount = Product.objects.filter(id__in=cid).values_list('price',flat=True)
        amt=0
        for i in amount:
            amt=amt+i
        return render(request,'user/cart.html',{'cdata':cartdata,'amt':amt}) 
    else:
        return HttpResponseRedirect('/')

def RemoveCart(request,id):
    if request.user.is_authenticated:
        if request.method == "POST":
            Cart.objects.filter(product_id=id).delete()
            return HttpResponseRedirect('/cart/')
    else:
        return HttpResponseRedirect('/')
    
def ComponetSearch(request):
    if request.user.is_authenticated:
        try:
            if request.method == "POST":
                search = request.POST.get('search')

                sdata = Product.objects.filter(Q(category=search) | Q(pname=search) | Q(desc__contains=search) |Q(price__contains=search))
                                                
                print(sdata)
            return render(request, 'user/search.html',{'sdata':sdata})
        except:
            return HttpResponseRedirect('/userindex/')
    else:
        return HttpResponseRedirect('/')
    
def Details(request,id):
    if request.user.is_authenticated:
        print(request.user)
        data_detail = Product.objects.filter(pk=id)
        print(data_detail)
        return render(request,'user/details.html',{'data':data_detail})
    else:
        return HttpResponseRedirect('/')

def SignUp(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/userindex/')
    else:
        if request.method == "POST":
            uname = request.POST.get('uname')
            email = request.POST.get('email')
            pass1 = request.POST.get('pass')
            print(uname,pass1,email)
            User.objects.create_user(uname,email,pass1)
            
            subject = f'Welcome To Pet Store {uname}'
            message = f"""
                    Dear {uname},
                        
                    You have successfully register to The_Pet_Store
                    with {email} this email,

                    Thank you for selecting The_Pet_Store

                    Happy Shopping...Keep Shopping...Stay In Touch

                    'Note: please do not reply to this mail because it is auto generated..'
                        
                    """
            mail_from = settings.EMAIL_HOST_USER
            mail_to = email
            send_mail(subject,message,mail_from,[mail_to])

            messages.success(request, 'SignUp Successfully')


        return render(request, 'user/signup.html')

def Login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/userindex/')
    else:
        if request.method == "POST":
            username = request.POST.get('uname')
            password = request.POST.get('pass') 
            user = authenticate(request, username=username, password=password) 
            if user is not None:
                login(request,user)
                return HttpResponseRedirect('/userindex/')
        return render(request,'user/login.html')

def Logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def address(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            cname = request.POST.get('cname')
            flat = request.POST.get('flat')
            landmark = request.POST.get('landmark')
            city = request.POST.get('city')
            state = request.POST.get('state')
            pincode = request.POST.get('pincode')
            contact = request.POST.get('contact')
            acontact = request.POST.get('acontact')
            # print(cname,flat,landmark,city,state,pincode,contact,acontact)
            Address.objects.create(user=request.user,name=cname,flat=flat,landmark=landmark,city=city,state=state,pincode=pincode,contact=contact,contactA=acontact)
        #here we are fetching data from address table
        data = Address.objects.filter(user_id=request.user)
        return render(request,'user/address.html',{'adata':data})
    else:
        return HttpResponseRedirect('/')
from django.shortcuts import render
from .models import Data
from myapp.forms import DataForm

# Create your views here.

def Forms(request):
    if request.method == "POST":
        fm = DataForm(request.POST)
        if fm.is_valid():
            fm.save()
            fm = DataForm()
    else:
        fm = DataForm()
        # print(fm)
    return render(request,'forms.html',{'fm':fm})


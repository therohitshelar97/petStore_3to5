from django.shortcuts import render

# Create your views here.
def Index(request):
    return render(request,'index.html')

def Home(request):
    data = "Hello People Welcome To Django Lecture"
    list1 = ['rahul','gopal','ramu','sham','khan','abdul']

    context = {'data':data,'data1':list1}
    return render(request,'home.html',context)

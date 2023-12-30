from django.shortcuts import render, HttpResponse

# Create your views here.
def Index2(request):
    print(request)
    return HttpResponse('Hello From Myapp2....')

def List(request):
    a = [1,2,3,3,4,4,5,5,6]
    return HttpResponse(a[:2])

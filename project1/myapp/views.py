from django.shortcuts import render, HttpResponse

# Create your views here.

def Index(request):
    print(request)
    return HttpResponse('Hello World!')

def Home(request):
    return HttpResponse('Welcomt To Home Page')

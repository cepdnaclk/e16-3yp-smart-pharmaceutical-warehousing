from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    #return HttpResponse('Home page')
    return render(request,"homepage.html")

def about(request):
    #return HttpResponse('about')
    return render(request,'about.html')
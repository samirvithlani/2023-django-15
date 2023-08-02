from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#django support 2 type of views !! function based views and class based views

def home(request):
    return HttpResponse("Home")

def aboutus(request):
    return render(request,"aboutus.html")

def contactUs(request):
    return render(request,"blog/contactUs.html")
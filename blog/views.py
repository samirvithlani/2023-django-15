from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
#django support 2 type of views !! function based views and class based views

def home(request):
    return HttpResponse("Home")

def aboutus(request):
    return render(request,"aboutus.html")

def contactUs(request):
    return render(request,"blog/contactUs.html")



def getProducts(request):
    products = Product.objects.all().values() #select * from product
    #product1 = Product.objects.get(id=1)
    #product1 = Product.objects.filter(name = "Iphone 14 pro")
    product1 = Product.objects.filter(name__icontains = "i")
    print(product1)
    context ={"products":products,"age":2} #dictionary
    return render(request,"blog/blogs.html",context)

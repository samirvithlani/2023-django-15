from django.contrib import admin
from django.urls import path,include
#import views for calling function 
from . import views

urlpatterns = [
 path('home/',views.home),
 path('aboutus/',views.aboutus),
 path('contactus/',views.contactUs),
 path('blogs/',views.getProducts),
]
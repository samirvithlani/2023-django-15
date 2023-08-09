from django.contrib import admin
from django.urls import path,include
#import views for calling function 
from .views import *

urlpatterns = [
    path ('addexp/',CreateExpense.as_view(),name='addexp'),
    path ('listexp/',ExpenseList.as_view(),name='listexp'),
]
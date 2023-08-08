from django.contrib import admin
from django.urls import path,include
from .views import ManagerRegisterView,UserLoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    
    path('manager_register/',ManagerRegisterView.as_view(),name='manager_register'),
    path('login/',UserLoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(next_page='login'),name='logout'),
 
]
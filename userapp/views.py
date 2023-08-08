from django.shortcuts import render
from .models import User
from .forms import ManagerCreatationForm
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView

# Create your views here.

class ManagerRegisterView(CreateView):
    model = User
    template_name = 'userapp/manager_register.html'
    form_class = ManagerCreatationForm
    success_url = '/'


class UserLoginView(LoginView):
    template_name = 'userapp/login.html'
    
    def get_redirect_url(self):
        print(self.request.user)
        if self.request.user.is_authenticated:
            print('user is authenticated')
            print("amanager --->",self.request.user.is_manager)
            #redirect to manager page
            if self.request.user.is_manager:
                return '/manager/'
            elif self.request.user.is_developer:
                #chamage url to developer
                return '/developer/'
            
        
        

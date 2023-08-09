from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from .models import User
from .forms import ManagerCreatationForm
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def home(request):
    return render(request,'home.html')

def sendMail(to):
    subject = 'welcome to app'
    message = 'Hi this is welcome mail'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [to,]
    send_mail( subject, message, email_from, recipient_list )
    return True

class ManagerRegisterView(CreateView):
    model = User
    template_name = 'userapp/manager_register.html'
    form_class = ManagerCreatationForm
    success_url = '/'
    
    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        print(email)
        sendMail(email)
        return super().form_valid(form)


class UserLoginView(LoginView):
    template_name = 'userapp/login.html'
    
    def get_success_url(self):
        if self.request.user.is_authenticated:
            if self.request.user.is_superuser:
                return '/admin/'
            elif self.request.user.is_manager:
                return '/manager/'
            elif self.request.user.is_developer:
                return '/developer/'    
        else:
            return '/login/'    
        

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.db import transaction

class ManagerCreatationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields =["username","email","contact","password1","password2"]
        
    
    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_manager = True
        if commit:
            user.save() # save the user
        return user    
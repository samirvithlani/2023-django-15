from django.shortcuts import render
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.views.generic import ListView, DetailView
from .models import Student

# Create your views here.
class RegisterStudent(CreateView):
    template_name = "student/register.html" #form
    model = Student #db entry , form
    success_url ="/student/list"
    #fields = ["name","email","password","age"]
    fields = "__all__"

class ListStudent(ListView):
    context_object_name = "students"
    model = Student
    template_name = "student/list.html"


class DeleteStudent(DeleteView):    
    model = Student
    template_name = "student/delete.html"
    success_url = "/student/list"
    
    #get method...

class UpdateStudent(UpdateView):
    template_name = "student/update.html"
    success_url = "/student/list"
    model = Student
    fields = "__all__"  
    

class DetailStudent(DetailView):     
    model = Student
    template_name ="student/detail.html" 
    context_object_name = "student"

    
from django.shortcuts import render
from django.views.generic import CreateView
from .models import Expense
from .forms import CreateExpenseForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView

# Create your views here.
@method_decorator(login_required(login_url="login"),name='dispatch')
class CreateExpense(CreateView):
    model = Expense
    template_name = 'expense/create_expense.html'
    form_class = CreateExpenseForm
    success_url = '/'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ExpenseList(ListView):
    model = Expense
    template_name = 'expense/expense_list.html'
    form_class = CreateExpenseForm
    success_url = '/'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #select * from expense where user = self.request.user
        context['expenses'] = Expense.objects.filter(user=self.request.user)
        return context    

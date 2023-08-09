from django.forms import ModelForm
from .models import Expense

class CreateExpenseForm(ModelForm):
    class Meta:
        fields = ["name","amount","category"]
        model = Expense
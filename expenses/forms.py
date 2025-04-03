from django import forms
from .models import Expense
from .models import Income

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['title', 'amount', 'category', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'style': 'text-transform: capitalize;'}),
            'category': forms.TextInput(attrs={'style': 'text-transform: uppercase;'}),
        }

class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['title', 'amount', 'category', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'style': 'text-transform: capitalize;'}),
            'category': forms.TextInput(attrs={'style': 'text-transform: uppercase;'}),
        }


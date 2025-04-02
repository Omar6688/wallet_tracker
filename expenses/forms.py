from django import forms
from .models import Expense

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['title', 'amount', 'category', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'style': 'text-transform: capitalize;'}),
            'category': forms.TextInput(attrs={'style': 'text-transform: uppercase;'}),
        }

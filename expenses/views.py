from django.shortcuts import render, redirect
from .models import Expense  

def index(request):
    expenses = Expense.objects.all().order_by('-date')  # get all expenses
    return render(request, 'expenses/index.html', {'expenses': expenses})  # send to template

from .forms import ExpenseForm  # import the form

def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('expenses')  # name of the index URL
    else:
        form = ExpenseForm()
    return render(request, 'expenses/add_expense.html', {'form': form})


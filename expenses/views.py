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
            expense = form.save(commit=False)
            # Modify the fields before saving to DB
            expense.title = expense.title.capitalize()
            expense.category = expense.category.upper()
            expense.save()
            return redirect('expenses')
    else:
        form = ExpenseForm()
    return render(request, 'expenses/add_expense.html', {'form': form})


from django.shortcuts import get_object_or_404

def edit_expense(request, expense_id):
    expense = get_object_or_404(Expense, pk=expense_id)

    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            updated_expense = form.save(commit=False)
            updated_expense.title = updated_expense.title.capitalize()
            updated_expense.category = updated_expense.category.upper()
            updated_expense.save()
            return redirect('expenses')
    else:
        form = ExpenseForm(instance=expense)

    return render(request, 'expenses/edit_expense.html', {'form': form, 'expense': expense})


def delete_expense(request, expense_id):
    expense = get_object_or_404(Expense, pk=expense_id)

    if request.method == 'POST':
        expense.delete()
        return redirect('expenses')

    return render(request, 'expenses/delete_expense.html', {'expense': expense})

from .models import Income

def income_list(request):
    incomes = Income.objects.all().order_by('-date')
    return render(request, 'expenses/income_list.html', {'incomes': incomes})

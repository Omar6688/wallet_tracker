from django.shortcuts import render, redirect
from .models import Expense
from .forms import IncomeForm
from django.contrib import messages


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

from django.contrib.auth.decorators import login_required

@login_required
def add_income(request):
    if request.method == 'POST':
        form = IncomeForm(request.POST)
        if form.is_valid():
            income = form.save(commit=False)
            income.user = request.user
            income.title = income.title.capitalize()
            income.category = income.category.upper()
            income.save()
            messages.success(request, 'Income added successfully!')
            return redirect('income_list')
    else:
        form = IncomeForm()
    return render(request, 'expenses/add_income.html', {'form': form})

from django.shortcuts import get_object_or_404

@login_required
def edit_income(request, income_id):
    income = get_object_or_404(Income, pk=income_id)

    if request.method == 'POST':
        form = IncomeForm(request.POST, instance=income)
        if form.is_valid():
            updated_income = form.save(commit=False)
            updated_income.user = request.user
            updated_income.title = updated_income.title.capitalize()
            updated_income.category = updated_income.category.upper()
            updated_income.save()
            messages.success(request, 'Income updated successfully!')
            return redirect('income_list')
    else:
        form = IncomeForm(instance=income)

    return render(request, 'expenses/edit_income.html', {'form': form, 'income': income})

@login_required
def delete_income(request, income_id):
    income = get_object_or_404(Income, pk=income_id)
    income.delete()
    messages.success(request, 'Income deleted successfully.')
    return redirect('income_list')



from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Sum

from .models import Expense, Income
from .forms import ExpenseForm, IncomeForm


# Expenses Home Page (Index) — shows totals and balance
@login_required
def index(request):
    expenses = Expense.objects.filter(user=request.user).order_by('-date')

    # Filter by category
    category = request.GET.get('category')
    if category:
        expenses = expenses.filter(category__icontains=category)

    # Filter by date
    date = request.GET.get('date')
    if date:
        expenses = expenses.filter(date=date)

    total_expenses = expenses.aggregate(total=Sum('amount'))['total'] or 0
    total_income = Income.objects.filter(user=request.user).aggregate(total=Sum('amount'))['total'] or 0
    balance = total_income - total_expenses

    return render(request, 'expenses/index.html', {
        'expenses': expenses,
        'total_expenses': total_expenses,
        'balance': balance
    })



# Add Expense
@login_required
def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.title = expense.title.capitalize()
            expense.category = expense.category.upper()
            expense.save()
            messages.success(request, 'Expense added successfully!')
            return redirect('expenses')
    else:
        form = ExpenseForm()
    return render(request, 'expenses/add_expense.html', {'form': form})


# Edit Expense
@login_required
def edit_expense(request, expense_id):
    expense = get_object_or_404(Expense, pk=expense_id)

    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            updated_expense = form.save(commit=False)
            updated_expense.title = updated_expense.title.capitalize()
            updated_expense.category = updated_expense.category.upper()
            updated_expense.save()
            messages.success(request, 'Expense updated successfully!')
            return redirect('expenses')
    else:
        form = ExpenseForm(instance=expense)

    return render(request, 'expenses/edit_expense.html', {'form': form, 'expense': expense})


# Delete Expense
@login_required
def delete_expense(request, expense_id):
    expense = get_object_or_404(Expense, pk=expense_id)

    if request.method == 'POST':
        expense.delete()
        messages.success(request, 'Expense deleted successfully.')
        return redirect('expenses')

    return render(request, 'expenses/delete_expense.html', {'expense': expense})


# Income List Page (with total)
@login_required
def income_list(request):
    incomes = Income.objects.filter(user=request.user).order_by('-date')

    # Filter by category
    category = request.GET.get('category')
    if category:
        incomes = incomes.filter(category__icontains=category)

    # Filter by date
    date = request.GET.get('date')
    if date:
        incomes = incomes.filter(date=date)

    total_income = incomes.aggregate(total=Sum('amount'))['total'] or 0

    return render(request, 'expenses/income_list.html', {
        'incomes': incomes,
        'total_income': total_income,
    })



# Add Income
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


# Edit Income
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


# Delete Income
@login_required
def delete_income(request, income_id):
    income = get_object_or_404(Income, pk=income_id)
    income.delete()
    messages.success(request, 'Income deleted successfully.')
    return redirect('income_list')

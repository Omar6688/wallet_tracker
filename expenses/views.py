from django.shortcuts import render
from .models import Expense  

def index(request):
    expenses = Expense.objects.all().order_by('-date')  # get all expenses
    return render(request, 'expenses/index.html', {'expenses': expenses})  # send to template

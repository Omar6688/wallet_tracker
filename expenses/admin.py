from django.contrib import admin
from .models import Expense, Income


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('title', 'amount', 'category', 'date')
    search_fields = ('title', 'category')
    list_filter = ('category', 'date')


@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ('title', 'amount', 'category', 'date')
    search_fields = ('title', 'category')
    list_filter = ('category', 'date')

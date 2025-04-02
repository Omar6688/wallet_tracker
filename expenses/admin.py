from django.contrib import admin
from .models import Expense

# Register your models here.

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('title', 'amount', 'category', 'date')
    search_fields = ('title', 'category')
    list_filter = ('category', 'date')
from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator



# Create your models here.


class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)])
    category = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - ${self.amount}"
  

class Income(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)])
    category = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.title} - ${self.amount}"

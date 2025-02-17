from django.contrib import admin
from apps.incomes.models import Incomes 
from apps.expenses.models import Expenses

# Register your models here.

admin.site.register(Incomes)
admin.site.register(Expenses)
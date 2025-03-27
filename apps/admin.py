from django.contrib import admin
from apps.incomes.models import Incomes 
from apps.expenses.models import Expenses
from apps.balance.models import Balance

# Register your models here.

admin.site.register(Incomes)
admin.site.register(Expenses)
admin.site.register(Balance)
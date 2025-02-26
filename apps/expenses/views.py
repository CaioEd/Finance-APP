from rest_framework import viewsets
from .models import Expenses
from .serializer import ExpenseSerializer


class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expenses.objects.all()
    serializer_class = ExpenseSerializer
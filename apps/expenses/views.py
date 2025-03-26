from django.utils.timezone import now
from django.db.models import Sum

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Expenses
from .serializer import ExpenseSerializer


class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expenses.objects.all()
    serializer_class = ExpenseSerializer


class TotalExpensesView(APIView):
    def get(self, request, *args, **kwargs):
        today = now()
        month_expenses = (
            Expenses.objects.filter(
                created_at__year=today.year, 
                created_at__month=today.month
            ).aggregate(total=Sum("value"))["total"] or 0
        )

        return Response({"total_expenses": month_expenses})
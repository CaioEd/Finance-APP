from django.utils.timezone import now
from django.db.models import Sum

from rest_framework.response import Response
from rest_framework.views import APIView

from .expenses.models import Expenses
from .incomes.models import Incomes


class TotalBalanceView(APIView):
    def get(self, request, *args, **kwargs):
        today = now()

        month_expenses = (
            Expenses.objects.filter(
                created_at__year=today.year, 
                created_at__month=today.month
            ).aggregate(total=Sum("value"))["total"] or 0
        )

        month_incomes = (
            Incomes.objects.filter(
                created_at__year=today.year, created_at__month=today.month
            ).aggregate(total=Sum("value"))["total"] or 0
        )

        total_balance = month_incomes - month_expenses

        return Response({"total_balance": total_balance})
    

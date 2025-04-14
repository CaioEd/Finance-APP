from django.utils.timezone import now
from django.db.models import Sum

from datetime import datetime

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
    

class FilterBalanceByDateView(APIView):
    def get(self, request, *args, **kwargs):

        start_date_str = request.query_params.get("start_date")
        end_date_str = request.query_params.get("end_date")

        if not start_date_str or not end_date_str:
            return Response({"error": "start_date and end_date are required"}, status=400)
        try:
            start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
            end_date = datetime.strptime(end_date_str, "%Y-%m-%d")
        except ValueError:
            return Response({"error": "Invalid date format. Use YYYY-MM-DD."}, status=400)

        start_month = start_date.replace(day=1)
        end_month = end_date.replace(end_date.replace(day=28) + timedelta(days=4)).replace(day=1) - timedelta(days=1)

        month_expenses = (
            Expenses.objects.filter(
                created_at__range=[start_month, end_month]
            ).aggregate(total=Sum("value"))["total"] or 0
        )

        month_incomes = (
            Incomes.objects.filter(
                created_at__range=[start_date, end_date]
            ).aggregate(total=Sum("value"))["total"] or 0
        )

        total_balance = month_incomes - month_expenses

        return Response({"total_balance": total_balance})
    

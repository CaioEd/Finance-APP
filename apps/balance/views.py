from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import datetime, timedelta
from django.utils.timezone import now
from django.db.models import Sum
from .models import Balance
from apps.expenses.models import Expenses
from apps.incomes.models import Incomes
from datetime import datetime

# OBTÉM OS BALANÇOS DE TODOS OS MESES, INCLUINDO RECEITAS E DESPESAS
class BalanceView(APIView):

    def get(self, request, *args, **kwargs):

        # Obter os anos e meses que possuem registros de incomes ou expenses
        months_with_data = (
            Incomes.objects.values('created_at__year', 'created_at__month')
            .union(Expenses.objects.values('created_at__year', 'created_at__month'))
        )

        balances = []
        
        for month_data in months_with_data:
            year = month_data['created_at__year']
            month = month_data['created_at__month']

            # Calcular os totais de incomes e expenses do mês
            total_incomes = Incomes.objects.filter(created_at__year=year, created_at__month=month).aggregate(total=Sum("value"))["total"] or 0
            total_expenses = Expenses.objects.filter(created_at__year=year, created_at__month=month).aggregate(total=Sum("value"))["total"] or 0
            total_balance = total_incomes - total_expenses
            
            # Verificar se já existe um registro de balance para esse mês
            existing_balance = Balance.objects.filter(data__year=year, data__month=month).first()

            if existing_balance:
                # Atualiza os valores se já existir um balance no banco
                existing_balance.total_income = total_incomes
                existing_balance.total_expense = total_expenses
                existing_balance.total_balance = total_balance
                existing_balance.save()
            else:
                # Criar um novo registro no Balance
                existing_balance = Balance.objects.create(
                    data=datetime(year, month, 1),
                    total_income=total_incomes,
                    total_expense=total_expenses,
                    total_balance=total_balance
                )

            balances.append({
                "month": existing_balance.data.strftime('%B %Y'),
                "total_income": existing_balance.total_income,
                "total_expense": existing_balance.total_expense,
                "total_balance": existing_balance.total_balance
            })

        return Response(balances)


# OBTÉM O BALANÇO DO MÊS ATUAL
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


# FILTRO POR DATA QUE OBTÉM O BALANÇO, RECEITAS E DESPESAS TOTAIS NO INTERVALO DE DATA DESEJADO
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
        next_month = end_date.replace(day=28) + timedelta(days=4)  # passa pro mês seguinte
        end_month = next_month.replace(day=1) - timedelta(days=1)  # volta pro último dia do mês original

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

        return Response({"total_balance": total_balance, "incomes": month_incomes, "expenses": month_expenses})
    
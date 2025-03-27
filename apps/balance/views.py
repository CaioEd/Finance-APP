from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Sum
from .models import Balance
from apps.expenses.models import Expenses
from apps.incomes.models import Incomes
from datetime import datetime


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

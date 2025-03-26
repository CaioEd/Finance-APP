from django.utils.timezone import now
from django.db.models import Sum

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Incomes
from .serializer import IncomeSerializer


class IncomeViewSet(viewsets.ModelViewSet):
    queryset = Incomes.objects.all()
    serializer_class = IncomeSerializer



class TotalIncomesView(APIView):
    def get(self, request, *args, **kwargs):  
        today = now()
        month_incomes = (
            Incomes.objects.filter(
                created_at__year=today.year, created_at__month=today.month
            ).aggregate(total=Sum("value"))["total"] or 0
        )

        return Response({"total_incomes": month_incomes})
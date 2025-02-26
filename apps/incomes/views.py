from rest_framework import viewsets
from .models import Incomes
from .serializer import IncomeSerializer


class IncomeViewSet(viewsets.ModelViewSet):
    queryset = Incomes.objects.all()
    serializer_class = IncomeSerializer
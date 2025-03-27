from django.db import models


class Balance(models.Model):
    data = models.DateField()
    total_income = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    total_expense = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    total_balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)


    def __str__(self):
        return f"Balance for {self.data.strftime("%B %Y")}"
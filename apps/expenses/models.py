from django.db import models

class Expenses(models.Model):
    title = models.CharField(max_length=50, verbose_name="Income Title")
    value = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Amount")
    category = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")

    def __str__(self):
        return f"{self.title} - {self.value}"
from django.contrib import admin
from django.urls import path
from .views import list_expenses, create_expense, edit_expense, delete_expense, get_expense_by_id

urlpatterns = [
    path('expenses/', list_expenses, name="list_expenses"),
    path('expense/', create_expense, name="create_expense"),
    path('edit_expense/<int:expense_id>/', edit_expense, name="edit_expense"),
    path('delete_expense/<int:expense_id>/', delete_expense, name="delete_expense"),
    path('expense/<int:expense_id>/', get_expense_by_id, name="get_expense_by_id"),
]

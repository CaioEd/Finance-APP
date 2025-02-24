from django.contrib import admin
from django.urls import path
from .views import list_incomes, create_income, edit_income, delete_income, get_income_by_id

urlpatterns = [
    path('incomes/', list_incomes, name="list_incomes"),
    path('income/', create_income, name="create_income"),
    path('edit_income/<int:income_id>/', edit_income, name="edit_income"),
    path('delete_income/<int:income_id>/', delete_income, name="delete_income"),
    path('income/<int:income_id>', get_income_by_id, name="get_income_by_id"),
]

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from models import Expenses
import json

@csrf_exempt
def list_expenses(request):
    expenses = Expenses.objects.values("id", "title", "value", "category", "created_at")
    return JsonResponse(list(expenses), safe=False)


@csrf_exempt
def create_expense(request):
    if request.method == "POST":
        data = json.loads(request.body)
        title = data.get("title")
        value = data.get("value")
        category = data.get("category")

        expense = Expenses(
            title=title, value=value, category=category
        )
        expense.save()
        return JsonResponse({"message": "Expense Created"}, status=201)
    return JsonResponse({"error": "Method Not Allowed"}, status=405)


def edit_expense(request, expense_id):
    try:
        expense = Expenses.objects.get(id=expense_id)
    except Expenses.DoesNotExist:
        return JsonResponse({"error": "Expense not found"}, status=404)

    if request.method == "PUT":
        data = json.loads(request.body)
        expense.title = data.get("title", expense.title)
        expense.value = data.get("value", expense.value)
        expense.category = data.get("category", expense.category)

        expense.save()
        return JsonResponse({"message": "Expense Update Ok"}, status=200)

    return JsonResponse({"error": "Method Not Allowed"}, status=405)


def delete_expense(request, expense_id):
    try:
        expense = Expenses.objects.get(id=expense_id)
    except Expenses.DoesNotExist:
        return JsonResponse({"error": "Expense not found"}, status=404)

    if request.method == "DELETE":
        expense.delete()
        return JsonResponse({"message": "Expense deleted successfully"}, status=200)

    return JsonResponse({"error": "Method Not Allowed"}, status=405)

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from models import Incomes
import json

@csrf_exempt
def list_incomes(request):
    incomes = Incomes.objects.values("id", "title", "value", "category", "created_at")

    return JsonResponse(list(incomes), safe=False)


@csrf_exempt
def create_income(request):
    if request.method == "POST":
        data = json.loads(request.body)
        title = data.get("title")
        value = data.get("value")
        category = data.get("category")

        income = Incomes(
            title=title, value=value, category=category
        )
        income.save()
        return JsonResponse({"message": "Income Created"}, status=201)
    return JsonResponse({"error": "Method not Allowed"}, status=405)


def edit_income(request, income_id):
    try:
        income = Incomes.objects.get(id=income_id)
    except Incomes.DoesNotExist:
        return JsonResponse({"error": "Income not found"}, status=404)
    
    if request.method == "PUT":
        data = json.loads(request.body)
        income.title = data.get("title", income.title)
        income.value = data.get("value", income.value)
        income.category = data.get("category", income.category)

        income.save()
        return JsonResponse({"message": "Income Update Ok"}, status=200)
    
    return JsonResponse({"error": "Method Not Allowed"}, status=405)


def delete_income(request, income_id):
    try:
        income = Incomes.objects.get(id=income_id)
    except Incomes.DoesNotExist:
        return JsonResponse({"error": "Income not found"}, status=404)
    
    if request.method == "DELETE":
        income.delete()
        return JsonResponse({"message": "Income deleted successfully"}, status=200)
    
    return JsonResponse({"error": "Method Not Allowed"}, status=405)
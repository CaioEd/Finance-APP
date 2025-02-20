from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json


@csrf_exempt
def register(request):
    if request.method == "POST":
        data = json.loads(request.body)
        first_name = data.get("first_name")
        username = data.get("username")
        email = data.get("email")
        password = data.get("password")

        if User.objects.filter(username=username).exists():
            return JsonResponse({"error": "User already exists"}, status=400)
        
        user = User(
            username=username, email=email, first_name=first_name
        )
        user.set_password(password)
        user.save()
        return JsonResponse({"message": "User Created"}, status=201)
    
    return JsonResponse({"error": "Method Not Allowed"}, status=405)


@csrf_exempt
def user_login(request):
    if request.method == "POST":
        data = json.loads(request.body)
        username = data.get("username")
        password = data.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return JsonResponse({"message": "Login Ok"}, status=200)
        else:
            return JsonResponse({"error": "Invalid Credentials"}, status=400)
        
    return JsonResponse({"error": "Method Not Allowed"}, statu=405)


@login_required
@csrf_exempt
def user_logout(request):
    logout(request)
    return JsonResponse({"message": "Logout Ok"}, status=200)


@login_required
def list_users(request):
    if not request.user.is_superuser:
        return JsonResponse({"error": "Access Denied"}, status=403)
    
    users = User.objects.values("id", "username", "first_name", "email")
    return JsonResponse(list(users), safe=False)


@login_required
@csrf_exempt
def edit_user(request, user_id):
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return JsonResponse({"error": "User not Found"}, status=404)
    
    if request.method == "PUT":
        data = json.loads(request.body)
        user.first_name = data.get("first_name", user.first_name)
        user.username = data.get("username", user.username)
        user.email = data.get("email", user.email)
        user.password = data.get("password", user.password)

        if "password" in data and data["password"]:
            user.set_password(data["password"])

        user.save()
        return JsonResponse({"message": "User Update Ok"}, status=200)
    
    return JsonResponse({"error": "Method Not Allowed"}, status=405)
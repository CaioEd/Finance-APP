from django.contrib import admin
from django.urls import path
from .views import list_users, register, user_login, edit_user, user_logout, get_user_by_id

urlpatterns = [
    path('users/', list_users, name="list_users"),
    path('register/', register, name="register"),
    path('login/', user_login, name="login"),
    path('logout/', user_logout, name="logout"),
    path('edit_user/<int:user_id>/', edit_user, name="edit_user"),
    path('user/<int:user_id>/', get_user_by_id, name="get_user_by_id"),
]

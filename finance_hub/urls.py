from django.contrib import admin
from django.urls import path, include

from apps.users.views import register_user, login_user
import apps.users.urls
import apps.expenses.urls
import apps.incomes.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/register/', register_user, name="register_user"),
    path('api/login/', login_user, name="login_user"),
    path('api/', include(apps.users.urls)),
    path('api/', include(apps.expenses.urls)),
    path('api/', include(apps.incomes.urls)),
]

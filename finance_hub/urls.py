import apps.balance
import apps.balance.views
import apps.expenses.views
from apps.users.views import register_user, login_user
import apps.users.urls
import apps.expenses.urls
import apps.incomes.urls
import apps.views

from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/register/', register_user, name="register_user"),
    path('api/login/', login_user, name="login_user"),
    path('api/', include(apps.users.urls)),
    path('api/', include(apps.expenses.urls)),
    path('api/', include(apps.incomes.urls)),
    path('api/incomes/month', apps.incomes.views.TotalIncomesView.as_view(), name="incomes_month"),
    path('api/expenses/month', apps.expenses.views.TotalExpensesView.as_view(), name="expenses_month"),
    path('api/balance/month/', apps.views.TotalBalanceView.as_view(), name="balance_month"), 
    path('balance/', apps.balance.views.BalanceView.as_view(), name="balance")
]

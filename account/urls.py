from django.urls import path

from . import views

urlpatterns = [
    path('accounts', views.find_all),
    path('<str:account_number>', views.get_account),
]

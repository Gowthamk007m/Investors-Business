from django.urls import path, include
from . import views

urlpatterns = [

    path('Banker', views.bankers_home, name='bankers_home'),
    path('loan_details', views.create_bank_loan, name='create_loan'),


]

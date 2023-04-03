from django.urls import path, include
from . import views

urlpatterns = [
    path('InvestorHome', views.Investors_Home, name='Investors_Home'),
    path('create_Investor_Offer/<str:business_id>', views.create_Investor_Offer, name='create_Investor_Offer'),
]

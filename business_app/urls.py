
from django.urls import path,include
from business_app import views

urlpatterns = [
    path('Business_Home',views.Business_Home,name='Business_Home'),
    path('Business_create',views.Business_Create,name='Business_create'),
    path('business_loan',views.business_loan,name='business_loan'),
    path('delete_business/<str:pk>',views.delete_business,name='delete_business'),
]

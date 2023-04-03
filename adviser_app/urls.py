from django.urls import path, include
from . import views

urlpatterns = [

    path('Advisor_Home', views.advisor_home, name='advisor_home'),
    path('advice_user/<str:pk>', views.create_reply, name='advice_user'),
    path('ideas', views.see_business, name='ideas'),


]

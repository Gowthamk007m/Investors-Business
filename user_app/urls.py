from django.urls import path, include
from . import views

urlpatterns = [

    path('Userhome', views.User_Home, name='User_Home'),
    path('Create_Query/<str:pk>', views.create_query, name='create_query'),

]

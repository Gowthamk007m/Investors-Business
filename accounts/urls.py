from django.urls import path
from accounts import views

urlpatterns = [

    path('', views.home, name='home'),
    path('login/', views.Login_page, name='login'),
    path('register/<int:pk>', views.register, name='register'),
    path('logout/', views.LogoutUser, name='logout'),

]

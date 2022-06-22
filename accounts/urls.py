from django.urls import path 
from . import views 

urlpatterns = [
    path('entrar/', views.user_login, name='login'),
    path('sair/', views.user_logout, name='logout'),
    path('cadastro/', views.register, name='register')
    
              ]
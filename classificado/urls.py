from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='home'), 
    path('Anunciar/', views.announce, name='announce'), 
    path('<str:Categoria>/', views.filter, name='category')
               ]
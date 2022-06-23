from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='home'), 
    path('Anunciar/', views.announce, name='announce'), 
    path('meus_anuncios/', views.my_ads, name='my_ads'),
    path('remover/<int:id>/', views.remove_ads,name='remove'),
    path('item/<str:title>_<int:id>/', views.item, name="item"),
    path('filtro/<str:Categoria>/', views.filter, name='category')
               ]
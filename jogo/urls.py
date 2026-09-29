# jogo/urls.py (criar este arquivo)
from django.urls import path
from . import views

urlpatterns = [
    path('', views.boas_vindas, name='boas_vindas'),
    path('jogar/', views.jogar, name='jogar') # ← nova rota
] 
from django.urls import path
from . import views
urlpatterns=[path('',views.painel,name='painel'),path('atendimentos/novo/',views.novo_atendimento,name='novo_atendimento'),path('clientes/<int:cliente_id>/historico/',views.historico,name='historico')]

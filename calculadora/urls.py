from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('adicao/', views.adicao, name='adicao'),
    path('subtracao/', views.subtracao, name='subtracao'),
    path('multiplicacao/', views.multiplicacao, name='multiplicacao'),
    path('divisao/', views.divisao, name='divisao'),
    path('adicao/calculoAdicao/', views.calculoAdicao, name='cAdi'),
    path('subtracao/calculoSubtracao/', views.calculoSubtracao, name='cSub'),
    path('multiplicacao/calculoMultiplicacao/', views.calculoMultiplicacao, name='cMul'),
    path('divisao/calculoDivisao/', views.calculoDivisao, name='cDiv'),
]
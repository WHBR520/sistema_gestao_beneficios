from django.urls import path
from .views import modelo_view, index_view, funcionarios_view, beneficios_view, departamentos_view, listagem_funcionarios, listagem_beneficios

urlpatterns = [
    # path('endereço/', MinhaView.as_view(), name='nome-da-url')  -  templateview(apaguei)
    # path('endereço/', views.nome-da-funcao, name='nome-da-url')
    path('modelo/', modelo_view, name='modelo'),
    path('', index_view, name='home'),
    path('funcionarios/', funcionarios_view, name='funcionarios'),
    path('listagem_funcionarios/', listagem_funcionarios, name='listagem_funcionarios'),
    path('beneficios/', beneficios_view, name='beneficios'),
    path('listagem_beneficios/', listagem_beneficios, name='listagem_beneficios'),
    path('departamentos/', departamentos_view, name='departamentos'),
]
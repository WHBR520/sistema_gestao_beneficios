from django.shortcuts import render
from .models import Beneficios, Departamentos, Funcionarios

#def funcoa(request):
#    nome do bagulho = NomedaTabela.objects.all()  -- para pegar todos os dados da tabela
#    return render(request, 'pasta/arquivo.html', {})

def modelo_view(request):
    funcionarios = Funcionarios.objects.all()
    print(funcionarios)
    return render(request, 'app_funcionarios_beneficios/modelo.html', {"funcionarios": funcionarios})

def index_view(request):
    return render(request, 'app_funcionarios_beneficios/index.html', {})

def funcionarios_view(request):
    funcionarios = Funcionarios.objects.all()
    print(funcionarios)
    return render(request, 'app_funcionarios_beneficios/funcionarios.html', {"funcionarios": funcionarios})

def listagem_funcionarios(request):
    novo_funcionario = Funcionarios()
    novo_funcionario.nome = request.POST.get('nome')
    novo_funcionario.telefone = request.POST.get('telefone')
    novo_funcionario.id = request.POST.get('id')
    novo_funcionario.save()
    # exbir funcionarios ja cadastrados na nova pagina
    funcionarios = {
        'funcionarios': Funcionarios.objects.all()
}
    return render(request, 'app_funcionarios_beneficios/listagem_funcionarios.html', funcionarios)

def beneficios_view(request):
    beneficios = Beneficios.objects.all()
    return render(request, 'app_funcionarios_beneficios/beneficios.html', {"beneficios": beneficios})

def listagem_beneficios(request):
    novo_beneficio = Beneficios()
    novo_beneficio.nome = request.POST.get('nome')
    novo_beneficio.valor = request.POST.get('valor')
    novo_beneficio.save()
    # exbir funcionarios ja cadastrados na nova pagina
    beneficios = {
        'beneficios': Beneficios.objects.all()
}
    return render(request, 'app_funcionarios_beneficios/listagem_beneficios.html', beneficios)

def departamentos_view(request):
    departamentos = Departamentos.objects.all()
    return render(request, 'app_funcionarios_beneficios/departamentos.html', {"departamentos": departamentos})
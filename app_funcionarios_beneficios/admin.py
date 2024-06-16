from django.contrib import admin
from app_funcionarios_beneficios.models import Beneficios, Departamentos, Telefone, Funcionarios

class BeneficiosAdmin(admin.ModelAdmin):
    ''' especifica os campos que devem ser exibidos na lista de objetos do painel de admin'''
    list_display = ['nome', 'valor', 'descricao']
    ''' especifica os campos que vao ser usados como 'base' para pesquisas '''
    search_fields = ['nome', 'valor']

class DepartamentosAdmin(admin.ModelAdmin):
    list_display = ['nome', 'descricao', 'setor']
    search_fields = ['nome', 'setor']

class TelefoneAdmin(admin.ModelAdmin):
    list_display = ['numero']
    search_fields = ['numero']

class FuncionariosAdmin(admin.ModelAdmin):
    list_display = ['nome', 'genero', 'id', 'telefone', 'departamentos_display', 'beneficios_display']
    search_fields = ['nome', 'id']
    ''' ja que o django nao permite exibir relacoes manytomany normalmente, precisa criar uma representaçao das tabelas, por  isso: '''
    ''' mas no caso a representaçao é apenas do atibuto nome e nao da tabela inteira e sim é necessario o nome _display '''
    def departamentos_display(self, obj):
        return ", ".join([depto.nome for depto in obj.departamentos.all()])

    def beneficios_display(self, obj):
        return ", ".join([beneficio.nome for beneficio in obj.beneficios.all()])


''' registrando as classes na interface do admin '''
admin.site.register(Beneficios, BeneficiosAdmin)
admin.site.register(Departamentos, DepartamentosAdmin)
admin.site.register(Telefone, TelefoneAdmin)
admin.site.register(Funcionarios, FuncionariosAdmin)
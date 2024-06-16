from django.db import models

class Beneficios(models.Model):
    nome = models.CharField(max_length=60, null=True)
    descricao = models.TextField()
    valor = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    ''' para o django saber que deve exibir o nome definido do beneficio e nao o nome do objeto padrao'beneficio(4)' '''
    def __str__(self):
        return self.nome
    ''' class meta para alterar/corrigir o nome das tabelas na interface de admin '''
    class Meta: 
        verbose_name = 'Benefício'
        verbose_name_plural = 'Benefícios'


class Departamentos(models.Model):
    SETORES = (
        ('A', 'Administrativo'),
        ('F', 'Financeiro'),
        ('R', 'Recursos Humanos'),
        ('P', 'Produção'),
        ('C', 'Comercial'),
    )
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    setor = models.CharField(max_length=1, choices=SETORES, default='P')

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'

class Telefone(models.Model):
    numero = models.CharField(max_length=13, null=False, blank=False)

    class Meta:
        verbose_name = 'Telefone'
        verbose_name_plural = 'Telefones'

    def __str__(self):
        return self.numero

class Funcionarios(models.Model):
    ''' variavel para criar opcoes de seleção '''
    SEXO_CHOICES = ( 
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    )
    nome = models.CharField(max_length=50, blank=False, null=True)
    genero = models.CharField(max_length=1, choices=SEXO_CHOICES, default='M')
    id = models.CharField(max_length=15, blank=False, null=False, primary_key=True)
    departamentos = models.ManyToManyField(Departamentos, blank=False)
    telefone = models.OneToOneField(Telefone, blank=True, null=True, on_delete=models.CASCADE)
    beneficios = models.ManyToManyField(Beneficios, blank=False)

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'
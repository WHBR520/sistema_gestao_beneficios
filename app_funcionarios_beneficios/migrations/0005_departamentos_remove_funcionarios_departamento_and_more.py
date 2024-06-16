# Generated by Django 5.0.6 on 2024-06-14 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_funcionarios_beneficios', '0004_alter_funcionarios_beneficios'),
    ]

    operations = [
        migrations.CreateModel(
            name='Departamentos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('descricao', models.TextField()),
                ('setor', models.CharField(choices=[('A', 'Administrativo'), ('F', 'Financeiro'), ('R', 'Recursos Humanos'), ('P', 'Produção'), ('C', 'Comercial')], default='P', max_length=1)),
            ],
            options={
                'verbose_name': 'Departamento',
                'verbose_name_plural': 'Departamentos',
            },
        ),
        migrations.RemoveField(
            model_name='funcionarios',
            name='departamento',
        ),
        migrations.AddField(
            model_name='funcionarios',
            name='departamento',
            field=models.ManyToManyField(to='app_funcionarios_beneficios.departamentos'),
        ),
    ]

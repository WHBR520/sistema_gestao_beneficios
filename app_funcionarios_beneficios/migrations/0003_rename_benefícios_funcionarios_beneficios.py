# Generated by Django 5.0.6 on 2024-06-14 18:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_funcionarios_beneficios', '0002_telefone_funcionarios_genero_alter_funcionarios_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='funcionarios',
            old_name='benefícios',
            new_name='beneficios',
        ),
    ]

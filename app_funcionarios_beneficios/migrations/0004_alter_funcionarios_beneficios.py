# Generated by Django 5.0.6 on 2024-06-14 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_funcionarios_beneficios', '0003_rename_benefícios_funcionarios_beneficios'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionarios',
            name='beneficios',
            field=models.ManyToManyField(to='app_funcionarios_beneficios.beneficios'),
        ),
    ]
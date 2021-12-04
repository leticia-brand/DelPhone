# Generated by Django 3.2.8 on 2021-12-04 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('delphone', '0002_auto_20211203_2347'),
    ]

    operations = [
        migrations.CreateModel(
            name='Busca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(help_text='Digite o estado', max_length=2)),
                ('cidade', models.CharField(help_text='Digite a cidade', max_length=200)),
                ('setor', models.CharField(max_length=30)),
            ],
            options={
                'ordering': ['estado'],
            },
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Digite o nome da empresa', max_length=100)),
                ('email', models.EmailField(help_text='Digite o email', max_length=50)),
                ('celular', models.CharField(help_text='Digite o celular (12)345678912', max_length=11)),
                ('endereco', models.CharField(help_text='Digite o endereço (rua e nº)', max_length=200)),
                ('estado', models.CharField(help_text='Digite o estado', max_length=2)),
                ('cidade', models.CharField(help_text='Digite a cidade', max_length=200)),
                ('setor', models.CharField(max_length=30)),
                ('n_funcionario', models.FloatField(help_text='Digite a quantidade de funcionários')),
                ('n_filiais', models.FloatField(help_text='Digite a quantidade de filiais')),
                ('data_criacao', models.DateField(help_text='Digite a data de criação')),
                ('faturamento_anual', models.FloatField(help_text='Digite o faturament anual (em milhares)')),
                ('horario_abertura', models.TimeField(help_text='Digite o horário de abertura')),
                ('horario_fechamento', models.TimeField(help_text='Digite o horário de fechamento')),
            ],
            options={
                'ordering': ['nome'],
            },
        ),
    ]

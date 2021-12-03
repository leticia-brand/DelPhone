# Generated by Django 3.2.9 on 2021-12-03 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delphone', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuário',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(help_text='Digite o estado', max_length=50)),
                ('cidade', models.CharField(help_text='Digite a cidade', max_length=50)),
                ('setor', models.CharField(help_text='Digite o setor desejado', max_length=30)),
            ],
            options={
                'ordering': ['setor'],
            },
        ),
        migrations.AlterField(
            model_name='empresa',
            name='celular',
            field=models.CharField(help_text='Digite o celular (12)345678912', max_length=11),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='email',
            field=models.EmailField(help_text='Digite o email', max_length=50),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='horario_func',
            field=models.TimeField(help_text='Digite o horário de funcionamento'),
        ),
    ]

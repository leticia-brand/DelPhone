from typing import Reversible
from faker import Faker
import random
import pandas as pd
from django.db import models

fake = Faker()


class Empresa (models.Model):
    nome = models.CharField(max_length=100, help_text='Digite o nome da empresa')
    email = models.EmailField(max_length=50, help_text='Digite o email')
    celular = models.CharField(max_length=11, help_text='Digite o celular (12)345678912')
    endereco = models.CharField(max_length=200, help_text='Digite o endereço (rua e nº)')
    estado =  models.CharField(max_length=2 , help_text='Digite o estado')
    cidade =  models.CharField(max_length=200, help_text='Digite a cidade')
    horario_func = models.TimeField(auto_now=False, auto_now_add=False, help_text='Digite o horário de funcionamento')
    setor = models.CharField(max_length=30, help_text='')

    objects = models.Manager()

    def get_absolute_url(self):
        """Returns the url to access a particular instance of Empresa."""
        return Reversible('empresa-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Empresa object (in Admin site etc.)."""
        return f'Nome: {self.nome} <br> Email: {self.email} <br> Celular: {self.celular} <br> Endereço: {self.endereco} <br> Estado: {self.estado} <br> Cidade: {self.cidade} <br> Horário de funcionamento: {self.horario_func} <br> Setor: {self.setor} '

    class Meta:
        ordering = ['nome']

'''class Usuário(models.Model):
    user = models.CharField(max_length=50, help_text='Digite o nome de usuario')
    cidade = models.CharField(max_length=50, help_text='Digite a cidade')
    def get_absolute_url(self):
        """Returns the url to access a particular instance of Empresa."""
        return reverse('usuario-detail', args=[str(self.id)])
    def __str__(self):
        """String for representing the Empresa object (in Admin site etc.)."""
        return self.user
    class Meta:
        ordering = ['user']
'''

estados = pd.read_excel (r'delphone/cidades_estados.xlsx').values.tolist()
setores = ['Alimentação', 'Cozinha', 'Eletrodomésticos', 'Esportes', 'Farmácia', 'Material de construção', 'Mobília', 'Música', 'Papelaria', 'Vestuário']



for i in range(200):
    n = random.randint(0, len(estados)-1)
    m = random.randint(0, len(setores)-1)
    p = Empresa  (nome=fake.company(), 
                email=fake.email(), 
                celular=fake.phone_number(), 
                endereco=fake.address(), 
                estado=estados[n][1], 
                cidade=estados[n][0], 
                horario_func=fake.date_time(), 
                setor=setores[m])
    '''p.save()
    Retiramos o comando pois ele adiciona rows todas as vezes'''


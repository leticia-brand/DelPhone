from faker import Faker

fake = Faker()

from django.db import models

class Empresa(models.Model):
    nome = models.CharField(max_length=100, help_text='Digite o nome da empresa')
    email = models.EmailField(max_length=50, help_text='Digite o email')
    celular = models.CharField(max_length=11, help_text='Digite o celular (12)345678912')
    endereco = models.CharField(max_length=200, help_text='Digite o endereço (rua e nº)')
    horario_func = models.TimeField(auto_now=False, auto_now_add=False, help_text='Digite o horário de funcionamento')
    setor = models.CharField(max_length=30, help_text='')

    def get_absolute_url(self):
        """Returns the url to access a particular instance of Empresa."""
        return reverse('empresa-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Empresa object (in Admin site etc.)."""
        return self.nome

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

for i in range(200):
    p = Empresa(nome=fake.name(), email=fake.email(), celular=fake.phone_number(), endereco=fake.address(), horario_func=fake.date_time(), setor=fake.job())
    p.save()
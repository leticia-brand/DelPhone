from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse
from django.http.response import HttpResponseNotFound, HttpResponseRedirect
from .models import Empresa
# Create your views here.


def menu (request):
    contexto = {"empresas": Empresa.objects.all()}
    return render(request, 'delphone/menu.html', contexto)

def contatos(request):
    dias_semana = ["SEGUNDA","TERÇA","QUARTA","QUINTA","SEXTA"]
    dias_final = ["SÁBADO", "DOMINGO"]
    horarios = ["9 - 18", "9 - 13"]
    context = {"dias_semana": dias_semana, "dias_final": dias_final, "horarios": horarios}
    return render(request, 'delphone/contatos.html', context)

def faq(request):
    return render(request, 'delphone/faq.html')
    
def login(request):
    return render(request, 'delphone/login.html')

def cadastro(request):
    all_entries = Empresa.objects.all().count()
    context = {'empresas': all_entries}
    return render(request, 'delphone/cadastro.html',context)

def como_funcionamos(request):
    return render(request, 'delphone/como_funcionamos.html')

def sobre_nos(request):
    return render(request, 'delphone/sobre_nos.html')

def redireciona(request):
    direcionamento = reverse('delphone')
    return HttpResponseRedirect(direcionamento)


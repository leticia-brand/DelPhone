from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse
from django.http.response import HttpResponseNotFound, HttpResponseRedirect
# Create your views here.

def index(request):
    return render(request, 'delphone/index.html')

def menu(request):
    return render(request, 'delphone/menu.html')

def contatos(request):
    return render(request, 'delphone/contatos.html')

def faq(request):
    return render(request, 'delphone/faq.html')
    
def login(request):
    return render(request, 'delphone/login.html')

def cadastro(request):
    return render(request, 'delphone/cadastro.html')

def como_funcionamos(request):
    return render(request, 'delphone/como_funcionamos.html')

def sobre_nos(request):
    return render(request, 'delphone/sobre_nos.html')


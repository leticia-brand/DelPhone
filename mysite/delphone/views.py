from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse
from django.http.response import HttpResponseNotFound, HttpResponseRedirect
# Create your views here.

def index(request):
    return render(request, 'delphone/index.html')

def cadastro(request):
    return render(request, 'delphone/cadastro.html')

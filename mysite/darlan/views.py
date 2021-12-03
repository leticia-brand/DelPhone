from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.http.response import HttpResponseNotFound, HttpResponseRedirect
# Create your views here.

def index(request):
    return render(request, "darlan/analysis.html")

def redireciona(request):
    direcionamento = reverse('darlan')
    return HttpResponseRedirect(direcionamento)

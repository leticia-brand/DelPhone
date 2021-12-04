from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.http.response import HttpResponseNotFound, HttpResponseRedirect
from delphone.models import Empresa, Busca
import pandas as pd

# Create your views here.

empresas = Empresa.objects.all().values()
empresas_df = pd.DataFrame(empresas)
empresas_dfh = empresas_df.head()

def  analise (request):
    contexto = {"empresas_dfh": empresas_dfh.to_html()}
    return render(request, "leticia/analysis.html", contexto)

def redireciona(request):
    direcionamento = reverse('leticia')
    return HttpResponseRedirect(direcionamento)
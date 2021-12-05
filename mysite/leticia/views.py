from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.http.response import HttpResponseNotFound, HttpResponseRedirect

# Create your views here.

def  analise (request):
    return render(request, "leticia/analise.html")

def redireciona(request):
    direcionamento = reverse('leticia')
    return HttpResponseRedirect(direcionamento)
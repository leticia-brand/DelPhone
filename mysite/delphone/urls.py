from django.urls import path

from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.menu, name='menu'),
    path('contatos/', views.contatos, name='contatos'),
    path('faq/', views.faq, name='faq'),
    path('login/', views.login, name='login'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('como_funcionamos/', views.como_funcionamos, name='como_funcionamos'),
    path('sobre_nos/', views.sobre_nos, name='sobre_nos')

    
]


urlpatterns += staticfiles_urlpatterns()

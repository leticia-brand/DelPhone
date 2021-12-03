from django.contrib import admin

from .models import Empresa, Usuário

admin.site.register(Empresa)
admin.site.register(Usuário)
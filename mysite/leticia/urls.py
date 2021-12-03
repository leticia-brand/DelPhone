from django.urls import include, path
from leticia import views

urlpatterns = [
    path("", views.analise, name ="analise"),
    path("redireciona/", views.redireciona, name="redireciona")
]
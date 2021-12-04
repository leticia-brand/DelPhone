from django.urls import include, path
from paloma import views

urlpatterns = [
    path("", views.index, name ="analysis-paloma"),
    path("index/", views.index, name ="index"),
    path("redireciona/", views.redireciona, name="redireciona")
]
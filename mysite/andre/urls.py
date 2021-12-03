from django.urls import include, path
from andre import views

urlpatterns = [
    path("", views.index, name ="index"),
    path("index/", views.index, name ="index"),
    path("redireciona/", views.redireciona, name="redireciona")
]
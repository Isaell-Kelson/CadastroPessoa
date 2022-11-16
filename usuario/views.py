from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Usuario

class ListaUsuarioView(ListView):
    model = Usuario
    queryset = Usuario.objects.all().order_by('login')


class UsuarioCreateView(CreateView):
    modele = Usuario
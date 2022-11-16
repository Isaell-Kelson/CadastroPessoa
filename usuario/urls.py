from django.urls import path
from .views import ListaUsuarioView


urlpatterns = [
    path('', ListaUsuarioView.as_view(), name='usuario.index')
]

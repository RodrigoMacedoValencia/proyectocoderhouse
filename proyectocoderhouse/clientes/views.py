from django.shortcuts import render
from .models import Pais, Cliente
# Create your views here.

def pais_list(request):
    paises = Pais.objects.all()
    contexto = {'paises': paises}
    return render(request, 'clientes/pais_list.html', contexto)
from django.shortcuts import render
from .models import Cliente
def index(request):
    clientes=Cliente.objects.all()
    dato={"clientes": clientes}
    return render(request, "cliente/index_cliente.html", dato)
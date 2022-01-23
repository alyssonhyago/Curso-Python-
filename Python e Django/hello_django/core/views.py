from django.shortcuts import render, HttpResponse

# Create your views here.
#.\\Scripts\Activate.ps1

def hello(request, nome,idade):
    return HttpResponse(f'<h1>Hello {nome} de {idade} anos</h1>')
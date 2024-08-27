from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    html="""
    <h1>Soy el index de la app1</h1>
    <h2>Hola!</h2>
    """
    return HttpResponse(html)

def pagina1(request):
    html="""
    <h1 style="color:blue">Soy la página 1</h1>
    """
    return HttpResponse(html)
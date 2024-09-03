from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'core/index.html')

def CategoriaAventura(request):
    return render(request, 'core/CategoriaAventura.html')

def Aventura1(request):
    return render(request, 'core/Aventura1.html')

def Aventura2(request):
    return render(request, 'core/Aventura2.html')

def CategoriaConduccion(request):
    return render(request, 'core/CategoriaConduccion.html')

def categoriaDeportes(request):
    return render(request, 'core/categoriaDeportes.html')

def CategoriaEstrategia(request):
    return render(request, 'core/CategoriaEstrategia.html')

def CategoriaInfantiles(request):
    return render(request, 'core/CategoriaInfantiles.html')

def Conduccion1(request):
    return render(request, 'core/Conduccion1.html')

def Conduccion2(request):
    return render(request, 'core/Conduccion2.html')

def Deporte1(request):
    return render(request, 'core/Deporte1.html')

def Deporte2(request):
    return render(request, 'core/Deporte2.html')

def Estrategia1(request):
    return render(request, 'core/Estrategia1.html')

def Estrategia2(request):
    return render(request, 'core/Estrategia2.html')

def Infantil1(request):
    return render(request, 'core/Infantil1.html')

def Infantil2(request):
    return render(request, 'core/Infantil2.html')

def login(request):
    return render(request, 'core/login.html')

def Principal(request):
    return render(request, 'core/Principal.html')

def recuperar_contrasena(request):
    return render(request, 'core/recuperar_contrasena.html')

def register(request):
    return render(request, 'core/register.html')


from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LogoutView
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationForm
from .models import Producto
from .forms import ProductoForm


import requests
from django.shortcuts import render

def Api(request):
    api_url = 'https://www.balldontlie.io/api/v1/teams'  # URL de la API que deseas consumir

    # Realizar solicitud GET a la API
    response = requests.get(api_url)

    # Procesar la respuesta de la API
    if response.status_code == 200:
        api_data = response.json()  # Convertir la respuesta JSON en un diccionario
        # Realizar cualquier procesamiento adicional necesario
    else:
        api_data = None  # O manejar el caso de error de alguna otra forma

    return render(request, 'equipos.html', {'api_data': api_data})


def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'crud/lista_productos.html' , {'productos':productos})

def crear_producto(request):
    
    data = {
        'form' : ProductoForm()
    }
    
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "El producto ha sido guardado correctamente"
        else:
            data["form"] = formulario
    
    return render(request, 'crud/crear_producto.html', data)

def editar_producto(request, codigo):
    
    producto = get_object_or_404(Producto, codigo=codigo)
    
    data = {
        'form' : ProductoForm(instance=producto)
    }
    if request.method =='POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] ="Modificado correctamente"
            return redirect(to="lista_productos")    
        data["form"] = formulario
    
    return render(request, 'crud/editar_producto.html',data)

def eliminar_producto(request, codigo):
    producto = get_object_or_404(Producto, codigo=codigo)
    if request.method == 'POST':
        producto.delete()
        return redirect('lista_productos')
    return render(request, 'crud/eliminar_producto.html', {'producto': producto})

    # Login - logout
def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Cambia 'login' por la ruta a tu página de inicio de sesión
    else:
        form = RegistrationForm()
    return render(request, 'crud/registro.html', {'form': form})




def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('inicio')  # Cambia 'inicio' por la ruta a tu página de inicio
        else:
            error_message = 'Credenciales inválidas'
    else:
        error_message = None
    return render(request, 'crud/login.html', {'error_message': error_message})





#............//
def estadio(request):
    return render (request,'app/estadio.html')

def base (request):
    return render (request,'app/base.html')

def jugadores (request):
    return render (request,'app/jugadores.html')

def inicio(request):
    return render (request,'app/inicio.html')
def socio(request):
    return render (request,'app/socio.html')
def equipos(request):
    return render (request,'app/equipos.html')
def entradas(request):
    return render (request,'app/entradas.html')





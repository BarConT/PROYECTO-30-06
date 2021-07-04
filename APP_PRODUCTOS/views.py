from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ProductoForm 
from django.contrib import messages

# Create your views here.


def agregar(request):
    data = {
            'form': ProductoForm()
            }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Producto agregado") 
            return redirect(to='principal')
        else:
            data["form"] = formulario
    return render(request, 'agregar.html', data)

def visualizar(request, id):
    producto = Producto.objects.all().filter(id=id)
    print(producto)
    

    data = {
            'producto': producto 
            }

    return render(request, 'visualizar.html', data)

def editar(request, id):

    producto = get_object_or_404(Producto, id=id)

    data = {
            'form': ProductoForm(instance=producto)
            }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado correctamente")
            return redirect(to="principal")
        data["form"] = formulario

    return render(request, 'editar.html', data)

def borrar(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    messages.success(request, "Eliminado correctamente")
    return redirect(to="principal")




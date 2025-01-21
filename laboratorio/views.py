from django.shortcuts import render, redirect
from .forms import Laboratorio_Form, DirectorGeneral_Form, Producto_Form
from .models import *
from django.views.generic import CreateView
from django.shortcuts import render, get_object_or_404

# Create your views here.
def app_index(request):
    return render(request, 'index.html')

#=======================================================================================================================================
# Vistas para Laboratorio
#=======================================================================================================================================

def listar_laboratorio(request, *args, **kwargs):
    '''Lista laboratorio.'''
    
    object_list = Laboratorio.objects.all() # Lista de objetos
    
    context = {
        'page' : 'Laboratorio',
        'singular' : 'laboratorio',
        'plural' : 'laboratorios',
        'url_listar' : 'listar_laboratorio',
        'url_crear' : 'crear_laboratorio',
        'url_ver' : 'ver_laboratorio',
        'url_editar' : 'modificar_laboratorio',
        'url_eliminar' : 'eliminar_laboratorio',
        'object_list': object_list
    }
    return render(request, 'generic_list.html', context)


def ver_laboratorio(request, id, *args, **kwargs):
    '''Detalle de laboratorio.'''
    
    itemObj = Laboratorio.objects.get(id=id) 
    
    context = {
        'page' : 'Detalle de Laboratorio',
        'singular' : 'laboratorio',
        'plural' : 'laboratorios',
        'url_listar' : 'listar_laboratorio',
        'url_crear' : 'crear_laboratorio',
        'url_ver' : 'ver_laboratorio',
        'url_editar' : 'modificar_laboratorio',
        'url_eliminar' : 'eliminar_laboratorio',
        'item': itemObj
    }
    return render(request, 'generic_detail.html', context)


def crear_laboratorio(request, *args, **kwargs):
    '''Crear laboratorio.'''
    
    form = Laboratorio_Form()
    
    if request.method == 'POST':
        form = Laboratorio_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_laboratorio')

    context = {
        'page' : 'Crear Laboratorio',
        'singular' : 'laboratorio',
        'plural' : 'laboratorios',
        'url_listar' : 'listar_laboratorio',
        'url_crear' : 'crear_laboratorio',
        'url_ver' : 'ver_laboratorio',
        'url_editar' : 'modificar_laboratorio',
        'url_eliminar' : 'eliminar_laboratorio',
        'form': form
    }
    return render(request, 'generic_form.html', context)
    

def modificar_laboratorio(request, id, *args, **kwargs):
    '''Editar laboratorio.'''
    
    itemObj = Laboratorio.objects.get(id=id) 
    form = Laboratorio_Form(instance=itemObj)
    
    if request.method == 'POST':
        form = Laboratorio_Form(request.POST, instance=itemObj)
        if form.is_valid():
            form.save()
            return redirect('listar_laboratorio')

    context = {
        'page' : 'Editar Laboratorio',
        'singular' : 'laboratorio',
        'plural' : 'laboratorios',
        'url_listar' : 'listar_laboratorio',
        'url_crear' : 'crear_laboratorio',
        'url_ver' : 'ver_laboratorio',
        'url_editar' : 'modificar_laboratorio',
        'url_eliminar' : 'eliminar_laboratorio',
        'item': itemObj,
        'form': form,
    }
    return render(request, 'generic_form.html', context)


def eliminar_laboratorio(request, id, *args, **kwargs):
    '''Eliminar laboratorio.'''
    
    itemObj = Laboratorio.objects.get(id=id) 
    
    if request.method == 'POST':
        itemObj.delete()
        return redirect('listar_laboratorio')

    context = {
        'page' : 'Eliminar Laboratorio',
        'singular' : 'laboratorio',
        'plural' : 'laboratorios',
        'url_listar' : 'listar_laboratorio',
        'url_crear' : 'crear_laboratorio',
        'url_ver' : 'ver_laboratorio',
        'url_editar' : 'modificar_laboratorio',
        'url_eliminar' : 'eliminar_laboratorio',
        'item': itemObj,
    }
    return render(request, 'generic_delete_object.html', context)

#=======================================================================================================================================
# Vistas para Director General
#=======================================================================================================================================

def listar_director(request, *args, **kwargs):
    '''Lista director.'''
    
    object_list = DirectorGeneral.objects.all() # Lista de objetos
    
    context = {
        'page' : 'Director General',
        'singular' : 'director general',
        'plural' : 'directores generales',
        'url_listar' : 'listar_director',
        'url_crear' : 'crear_director',
        'url_ver' : 'ver_director',
        'url_editar' : 'modificar_director',
        'url_eliminar' : 'eliminar_director',
        'object_list': object_list
    }
    return render(request, 'generic_list.html', context)


def ver_director(request, id, *args, **kwargs):
    '''Detalle de director.'''
    
    itemObj = DirectorGeneral.objects.get(id=id) 
    
    context = {
        'page' : 'Detalle de Director General',
        'singular' : 'director general',
        'plural' : 'directores generales',
        'url_listar' : 'listar_director',
        'url_crear' : 'crear_director',
        'url_ver' : 'ver_director',
        'url_editar' : 'modificar_director',
        'url_eliminar' : 'eliminar_director',
        'item': itemObj
    }
    return render(request, 'generic_detail.html', context)


def crear_director(request, *args, **kwargs):
    '''Crear director.'''
    
    form = DirectorGeneral_Form()
    
    if request.method == 'POST':
        form = DirectorGeneral_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_director')

    context = {
        'page' : 'Crear Director General',
        'singular' : 'director general',
        'plural' : 'directores generales',
        'url_listar' : 'listar_director',
        'url_crear' : 'crear_director',
        'url_ver' : 'ver_director',
        'url_editar' : 'modificar_director',
        'url_eliminar' : 'eliminar_director',
        'form': form
    }
    return render(request, 'generic_form.html', context)
    

def modificar_director(request, id, *args, **kwargs):
    '''Editar director.'''
    
    itemObj = DirectorGeneral.objects.get(id=id) 
    form = DirectorGeneral_Form(instance=itemObj)
    
    if request.method == 'POST':
        form = DirectorGeneral_Form(request.POST, instance=itemObj)
        if form.is_valid():
            form.save()
            return redirect('listar_director')

    context = {
        'page' : 'Editar Director General',
        'singular' : 'director general',
        'plural' : 'directores generales',
        'url_listar' : 'listar_director',
        'url_crear' : 'crear_director',
        'url_ver' : 'ver_director',
        'url_editar' : 'modificar_director',
        'url_eliminar' : 'eliminar_director',
        'item': itemObj,
        'form': form,
    }
    return render(request, 'generic_form.html', context)


def eliminar_director(request, id, *args, **kwargs):
    '''Eliminar director.'''
    
    itemObj = DirectorGeneral.objects.get(id=id) 
    
    if request.method == 'POST':
        itemObj.delete()
        return redirect('listar_director')

    context = {
        'page' : 'Eliminar Director General',
        'singular' : 'director general',
        'plural' : 'directores generales',
        'url_listar' : 'listar_director',
        'url_crear' : 'crear_director',
        'url_ver' : 'ver_director',
        'url_editar' : 'modificar_director',
        'url_eliminar' : 'eliminar_director',
        'item': itemObj,
    }
    return render(request, 'generic_delete_object.html', context)


#=======================================================================================================================================
# Vistas para Laboratorio
#=======================================================================================================================================

def listar_producto(request, *args, **kwargs):
    '''Lista Producto.'''
    
    object_list = Producto.objects.all() # Lista de objetos
    
    context = {
        'page' : 'Producto',
        'singular' : 'producto',
        'plural' : 'productos',
        'url_listar' : 'listar_producto',
        'url_crear' : 'crear_producto',
        'url_ver' : 'ver_producto',
        'url_editar' : 'modificar_producto',
        'url_eliminar' : 'eliminar_producto',
        'object_list': object_list
    }
    return render(request, 'generic_list.html', context)


def ver_producto(request, id, *args, **kwargs):
    '''Detalle de Producto.'''
    
    itemObj = Producto.objects.get(id=id) 
    
    context = {
        'page' : 'Detalle de Producto',
        'singular' : 'producto',
        'plural' : 'productos',
        'url_listar' : 'listar_producto',
        'url_crear' : 'crear_producto',
        'url_ver' : 'ver_producto',
        'url_editar' : 'modificar_producto',
        'url_eliminar' : 'eliminar_producto',
        'item': itemObj
    }
    return render(request, 'generic_detail.html', context)


def crear_producto(request, *args, **kwargs):
    '''Crear Producto.'''
    
    form = Producto_Form()
    
    if request.method == 'POST':
        form = Producto_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_producto')

    context = {
        'page' : 'Crear Producto',
        'singular' : 'producto',
        'plural' : 'productos',
        'url_listar' : 'listar_producto',
        'url_crear' : 'crear_producto',
        'url_ver' : 'ver_producto',
        'url_editar' : 'modificar_producto',
        'url_eliminar' : 'eliminar_producto',
        'form': form
    }
    return render(request, 'generic_form.html', context)
    

def modificar_producto(request, id, *args, **kwargs):
    '''Editar Producto.'''
    
    itemObj = Producto.objects.get(id=id) 
    form = Producto_Form(instance=itemObj)
    
    if request.method == 'POST':
        form = Producto_Form(request.POST, instance=itemObj)
        if form.is_valid():
            form.save()
            return redirect('listar_producto')

    context = {
        'page' : 'Editar Producto',
        'singular' : 'producto',
        'plural' : 'productos',
        'url_listar' : 'listar_producto',
        'url_crear' : 'crear_producto',
        'url_ver' : 'ver_producto',
        'url_editar' : 'modificar_producto',
        'url_eliminar' : 'eliminar_producto',
        'item': itemObj,
        'form': form,
    }
    return render(request, 'generic_form.html', context)


def eliminar_producto(request, id, *args, **kwargs):
    '''Eliminar Producto.'''
    
    itemObj = Producto.objects.get(id=id) 
    
    if request.method == 'POST':
        itemObj.delete()
        return redirect('listar_producto')

    context = {
        'page' : 'Eliminar Producto',
        'singular' : 'producto',
        'plural' : 'productos',
        'url_listar' : 'listar_producto',
        'url_crear' : 'crear_producto',
        'url_ver' : 'ver_producto',
        'url_editar' : 'modificar_producto',
        'url_eliminar' : 'eliminar_producto',
        'item': itemObj,
    }
    return render(request, 'generic_delete_object.html', context)

def laboratorio_detail(request, pk):
    laboratorio = get_object_or_404(Laboratorio, pk=pk)
    return render(request, 'laboratorio/detail.html', {'laboratorio': laboratorio})
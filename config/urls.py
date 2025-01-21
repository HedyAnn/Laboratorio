from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from laboratorio import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('lab/', include('laboratorio.urls')),

# Dashboard
    path('', views.app_index, name='app_index'),

#laboratorio
    path('listar_laboratorio/', views.listar_laboratorio, name='listar_laboratorio'),
    path('crear_laboratorio/', views.crear_laboratorio, name='crear_laboratorio'),
    path('ver_laboratorio/<int:id>/', views.ver_laboratorio, name='ver_laboratorio'),
    path('modificar_laboratorio/<int:id>/', views.modificar_laboratorio, name='modificar_laboratorio'),
    path('eliminar_laboratorio/<int:id>/', views.eliminar_laboratorio, name='eliminar_laboratorio'),

#Director General
    path('listar_director/', views.listar_director, name='listar_director'),
    path('crear_director/', views.crear_director, name='crear_director'),
    path('ver_director/<int:id>/', views.ver_director, name='ver_director'),
    path('modificar_director/<int:id>/', views.modificar_director, name='modificar_director'),
    path('eliminar_director/<int:id>/', views.eliminar_director, name='eliminar_director'),

#Productos  
    path('listar_producto/', views.listar_producto, name='listar_producto'),
    path('crear_producto/', views.crear_producto, name='crear_producto'),
    path('ver_producto/<int:id>/', views.ver_producto, name='ver_producto'),
    path('modificar_producto/<int:id>/', views.modificar_producto, name='modificar_producto'),
    path('eliminar_producto/<int:id>/', views.eliminar_producto, name='eliminar_producto'),

]

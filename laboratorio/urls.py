from django.urls import path
from . import views

app_name = 'laboratorio'

urlpatterns = [
    path('laboratorio/<int:id>/', views.ver_laboratorio, name='laboratorio_detail'),
]
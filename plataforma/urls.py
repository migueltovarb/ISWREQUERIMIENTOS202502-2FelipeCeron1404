from django.urls import path
from .views import (
    lista_proyectos,
    crear_proyecto,
    editar_proyecto,
    eliminar_proyecto,
    lista_tareas,
    crear_tarea,
    editar_tarea,
    eliminar_tarea,
)

app_name = 'plataforma'   # <-- NECESARIO PARA NAMESPACES

urlpatterns = [

    # PROYECTOS
    path('proyectos/', lista_proyectos, name='lista_proyectos'),
    path('proyectos/crear/', crear_proyecto, name='crear_proyecto'),
    path('proyectos/editar/<int:id>/', editar_proyecto, name='editar_proyecto'),
    path('proyectos/eliminar/<int:id>/', eliminar_proyecto, name='eliminar_proyecto'),

    # TAREAS
    path('proyectos/<int:id>/tareas/', lista_tareas, name='lista_tareas'),
    path('proyectos/<int:id>/tareas/crear/', crear_tarea, name='crear_tarea'),
    path('tareas/editar/<int:id>/', editar_tarea, name='editar_tarea'),
    path('tareas/eliminar/<int:id>/', eliminar_tarea, name='eliminar_tarea'),
]

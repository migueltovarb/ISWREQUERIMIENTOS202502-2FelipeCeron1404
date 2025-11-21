from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Proyecto, Tarea
from .forms import ProyectoForm, TareaForm


# ================================
#  PROYECTOS
# ================================

@login_required
def lista_proyectos(request):
    proyectos = Proyecto.objects.all()
    return render(request, 'plataforma/proyectos/lista_proyectos.html', {
        'proyectos': proyectos
    })


@login_required
def crear_proyecto(request):
    if request.method == 'POST':
        form = ProyectoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('plataforma:lista_proyectos')  
    else:
        form = ProyectoForm()

    return render(request, 'plataforma/proyectos/crear_proyecto.html', {
        'form': form
    })


@login_required
def editar_proyecto(request, id):
    proyecto = get_object_or_404(Proyecto, id=id)

    if request.method == 'POST':
        form = ProyectoForm(request.POST, instance=proyecto)
        if form.is_valid():
            form.save()
            return redirect('plataforma:lista_proyectos')   
    else:
        form = ProyectoForm(instance=proyecto)

    return render(request, 'plataforma/proyectos/editar_proyecto.html', {
        'form': form,
        'proyecto': proyecto
    })


@login_required
def eliminar_proyecto(request, id):
    proyecto = get_object_or_404(Proyecto, id=id)
    proyecto.delete()
    return redirect('plataforma:lista_proyectos')   



# ================================
#  TAREAS
# ================================

@login_required
def lista_tareas(request, id):
    proyecto = get_object_or_404(Proyecto, id=id)
    tareas = proyecto.tareas.all()

    return render(request, 'plataforma/tareas/lista_tareas.html', {
        'proyecto': proyecto,
        'tareas': tareas
    })


@login_required
def crear_tarea(request, id):
    proyecto = get_object_or_404(Proyecto, id=id)

    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            nueva_tarea = form.save(commit=False)
            nueva_tarea.proyecto = proyecto
            nueva_tarea.save()
            return redirect('plataforma:lista_tareas', id=proyecto.id)   

    else:
        form = TareaForm()

    return render(request, 'plataforma/tareas/crear_tarea.html', {
        'form': form,
        'proyecto': proyecto
    })


@login_required
def editar_tarea(request, id):
    tarea = get_object_or_404(Tarea, id=id)
    proyecto = tarea.proyecto

    if request.method == 'POST':
        form = TareaForm(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            return redirect('plataforma:lista_tareas', id=proyecto.id)   
    else:
        form = TareaForm(instance=tarea)

    return render(request, 'plataforma/tareas/editar_tarea.html', {
        'form': form,
        'tarea': tarea,
        'proyecto': proyecto
    })


@login_required
def eliminar_tarea(request, id):
    tarea = get_object_or_404(Tarea, id=id)
    proyecto_id = tarea.proyecto.id
    tarea.delete()
    return redirect('plataforma:lista_tareas', id=proyecto_id)   

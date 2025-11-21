from django.db import models
from django.conf import settings


class Proyecto(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField(blank=True, null=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(blank=True, null=True)

    ESTADOS = [
        ("PENDIENTE", "Pendiente"),
        ("EN_PROGRESO", "En progreso"),
        ("COMPLETADO", "Completado"),
    ]
    estado = models.CharField(max_length=20, choices=ESTADOS, default="PENDIENTE")

    PRIORIDAD = [
        ("BAJA", "Baja"),
        ("MEDIA", "Media"),
        ("ALTA", "Alta"),
    ]
    prioridad = models.CharField(max_length=10, choices=PRIORIDAD, default="MEDIA")

    # 🔥 Nuevo campo
    lider = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="proyectos_liderados"
    )

    def __str__(self):
        return self.nombre


class Tarea(models.Model):
    proyecto = models.ForeignKey(
        Proyecto, on_delete=models.CASCADE, related_name="tareas"
    )
    titulo = models.CharField(max_length=150)
    descripcion = models.TextField(blank=True, null=True)

    # 🔥 Cambiado para usar el usuario del sistema
    responsable = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="tareas_asignadas"
    )

    fecha_creacion = models.DateField(auto_now_add=True)
    fecha_entrega = models.DateField(blank=True, null=True)

    ESTADOS = [
        ("PENDIENTE", "Pendiente"),
        ("EN_PROGRESO", "En progreso"),
        ("COMPLETADA", "Completada"),
    ]
    estado = models.CharField(max_length=20, choices=ESTADOS, default="PENDIENTE")

    PRIORIDAD = [
        ("BAJA", "Baja"),
        ("MEDIA", "Media"),
        ("ALTA", "Alta"),
    ]
    prioridad = models.CharField(max_length=10, choices=PRIORIDAD, default="MEDIA")

    def __str__(self):
        return f"{self.titulo} ({self.proyecto.nombre})"

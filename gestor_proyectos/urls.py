from django.contrib import admin
from django.urls import path, include
from plataforma.views import lista_proyectos

urlpatterns = [
    path('admin/', admin.site.urls),

    # AUTENTICACIÓN
    path('accounts/', include(('accounts.urls', 'accounts'), namespace='accounts')),

    # DASHBOARD / INICIO
    path('', lista_proyectos, name='dashboard'),

    # PROYECTOS Y TAREAS
    path('plataforma/', include(('plataforma.urls', 'plataforma'), namespace='plataforma')),
]

from django.urls import path
from . import views

urlpatterns = [
    
    path("", views.inicio, name="home"),
    path("ver_cursos", views.ver_cursos, name="cursos"),
    #path("alta_curso/<nombre>", views.alta_curso), 
    path("alumnos",views.ver_alumnos, name ="alumnos"),
    path("profesores",views.ver_profesores, name ="profesores"),
    path("alta_curso", views.curso_formulario),
    path("buscar_curso", views.buscar_curso),
    path("buscar", views.buscar),
    path("alta_profesor", views.profesor_formulario),
    path("buscar_profesor", views.buscar_profe),
    path("buscar_prof", views.buscar_prof_final),
    path("alta_alumno", views.alumno_formulario),

  
]
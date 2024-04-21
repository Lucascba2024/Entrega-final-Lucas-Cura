from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from AppCoder.views import CustomLogoutView

urlpatterns = [
    
    path("", views.inicio, name="home"),
    path("ver_cursos", views.ver_cursos, name="cursos"),
    #path("alta_curso/<nombre>", views.alta_curso), 
    path("alumnos",views.ver_alumnos, name ="alumnos"),
    path("profesores",views.ver_profesores, name ="profesores"),
    #############curso###################
    path("alta_curso", views.curso_formulario),
    path("buscar_curso", views.buscar_curso),
    path("buscar", views.buscar),
    path("elimina_curso/<int:id>", views.elimina_curso, name= "elimina_curso"),
    path("editar_curso/<int:id>", views.editar_curso, name= "editar_curso"),
    
    #############profesor###################
    path("alta_profesor", views.profesor_formulario),
    path("buscar_profesor", views.buscar_profe),
    path("buscar_prof", views.buscar_prof_final),
    path("elimina_profesor/<int:id>", views.elimina_profesor, name= "elimina_profesor"),
    path("editar_profesor/<int:id>", views.editar_profesor, name= "editar_profesor"),
       
    #############Alumnos###################
    
    path("alta_alumno", views.alumno_formulario),
    path("buscar_alumno", views.buscar_alumno),
    path("buscar_al", views.buscar_alumno_final),
    path("elimina_alumno/<int:id>", views.elimina_alumno, name= "elimina_alumno"),
    path("editar_alumno/<int:id>", views.editar_alumno, name= "editar_alumno"),
    
    path("register", views.register , name="Register"),
    path('logout/', CustomLogoutView.as_view(), name='Logout'),
    path("login", views.login_request, name = "login" ),
    path("editarPerfil", views.editarPerfil, name="EditarPerfil")
    
    

  
]
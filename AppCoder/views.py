from django.shortcuts import render
from AppCoder.models import Curso, profesores , Alumnos
from django.http import HttpResponse
from django.template import loader
from AppCoder.forms import Curso_formulario , Profesor_formulario , AlumnoForm
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm
from django.contrib.auth import login, authenticate




# Create your views here.

def inicio (request):
    return render(request, "padre.html")

def alta_curso(request, nombre):
    curso= Curso(nombre= nombre , camada = 234512)
    curso.save()
    texto = f"Se Guardo en la BD el curso: {curso.nombre} {curso.camada}"
    return HttpResponse(texto)

def ver_cursos(request):
     cursos = Curso.objects.all()
     dicc ={"cursos": cursos}
     plantilla = loader.get_template ("cursos.html")
     documento = plantilla.render(dicc)
     return HttpResponse(documento)

def alumnos(request):
    return render(request, "alumnos.html") 

###################curso######################################
def curso_formulario(request):
    if request.method == "POST":
        mi_formulario = Curso_formulario(request.POST)

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            curso = Curso (nombre=datos["nombre"], camada = datos["camada"])
            curso.save()
            return render(request ,"formulario.html")
    return render(request ,"formulario.html")


def buscar_curso(request):
    return render(request, "buscar_curso.html")    


def buscar(request):
    if request.GET["nombre"]:
       nombre = request.GET["nombre"]
       cursos = Curso.objects.filter(nombre__icontains= nombre)
       return render( request , "resultado_busqueda.html" , {"cursos":cursos})
    else:
        return HttpResponse("Ingrese el nombre del curso")
          

###################profesor######################################
def profesor_formulario(request):
    if request.method == "POST":
        mi_formulario_pro = Profesor_formulario(request.POST)

        if mi_formulario_pro.is_valid():
            datos_pro = mi_formulario_pro.cleaned_data
            # Crea una instancia del modelo Profesor con los datos del formulario
            profesor = profesores(nombre=datos_pro["nombre"], camada=datos_pro["camada"])
            # Llama al método save() en la instancia del modelo Profesor
            profesor.save()
            return render(request, "formulario_profesores.html")
    return render(request, "formulario_profesores.html")
         
############ver profesores#############

def  ver_profesores(request):
     profesor = profesores.objects.all()
     dicc ={"profesores": profesor}
     plantilla = loader.get_template ("profesores.html")
     documento_pro = plantilla.render(dicc)
     return HttpResponse(documento_pro)  


#########pagina de busqueda#############
def buscar_profe(request):
    return render(request, "buscar_profesor.html")   

#########resultado busqueda#############    
def buscar_prof_final(request):
    if request.GET["nombre"]:
       nombre = request.GET["nombre"]
       profesor_encontrados = profesores.objects.filter(nombre__icontains=nombre)
       return render(request, "resultado_busqueda_prof.html", {"profesores": profesor_encontrados})
    else:
        return HttpResponse("Ingrese el nombre del Profesor")


     
#################alumnos################


def alumno_formulario(request):
    if request.method == "POST":
        mi_formulario_alumno = AlumnoForm(request.POST)

        if mi_formulario_alumno.is_valid():
            datos_alumno = mi_formulario_alumno.cleaned_data
            # Crea una instancia del modelo Alumno con los datos del formulario
            alumno = Alumnos(nombre=datos_alumno["nombre"], dni=datos_alumno["dni"])
            # Llama al método save() en la instancia del modelo Alumno
            alumno.save()
            return render(request, "formulario_alumnos.html")
    return render(request, "formulario_alumnos.html")


def ver_alumnos(request):
    alumnos = Alumnos.objects.all()  # Suponiendo que Alumno es el modelo de tu tabla de alumnos
    dicc_alumnos = {"alumnos": alumnos}
    plantilla = loader.get_template("alumnos.html")  # Asegúrate de tener una plantilla adecuada para mostrar la lista de alumnos
    documento_alumnos = plantilla.render(dicc_alumnos)
    return HttpResponse(documento_alumnos)


#########pagina de busqueda#############
def buscar_alumno(request):
    return render(request, "buscar_alumno.html")   

#########resultado busqueda#############    
def buscar_alumno_final(request):
    if request.GET["nombre"]:
       nombre = request.GET["nombre"]
       alumno_encontrados = Alumnos.objects.filter(nombre__icontains=nombre)
       return render(request, "resultado_busqueda_alum.html", {"alumnos": alumno_encontrados})
    else:
        return HttpResponse("Ingrese el nombre del Alumno")

#########loguin#############  

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")
            user = authenticate(username=usuario , password=contra)
            if user is not None:
                login(request , user )
                return render( request , "inicio.html" , {"mensaje":f"Bienvenido/a {usuario}"})
            else:
                return HttpResponse(f"Usuario no encontrado")
        else:
            return HttpResponse(f"FORM INCORRECTO {form}")

    form = AuthenticationForm()
    return render( request , "login.html" , {"form":form})

    ###########registro##########


def register(request):
    
    if request.method == "POST":
        pass
    else:
        form = UserCreationForm()
    return render(request , "registro.html" , {"form":form})
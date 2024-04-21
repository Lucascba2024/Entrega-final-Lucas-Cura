from django.shortcuts import render
from AppCoder.models import Curso, profesores , Alumnos , Avatar
from django.http import HttpResponse
from django.template import loader
from AppCoder.forms import Curso_formulario , Profesor_formulario , AlumnoForm, UserEditForm
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required


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
     avatares = Avatar.objects.filter(user=request.user.id)
     return render(request, 'cursos.html', {'cursos': cursos, 'url': avatares[0].imagen.url if avatares.exists() else None})



def alumnos(request):
    return render(request, "alumnos.html") 



############################################
###################curso####################
############################################

def curso_formulario(request):
    if request.method == "POST":
      
        mi_formulario = Curso_formulario(request.POST)

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data

            curso = Curso( nombre=datos["nombre"], camada=datos["camada"])
            curso.save()
            return render(request, "formulario.html")
    avatares = Avatar.objects.filter(user=request.user.id)
    return render(request, "formulario.html", {'url': avatares[0].imagen.url if avatares.exists() else None})


def buscar_curso(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    return render(request, 'buscar_curso.html', {'url': avatares[0].imagen.url if avatares.exists() else None})


def buscar(request):
    if request.GET["nombre"]:
       nombre = request.GET["nombre"]
       cursos = Curso.objects.filter(nombre__icontains= nombre)
       return render( request , "resultado_busqueda.html" , {"cursos":cursos})
    else:
        return HttpResponse("Ingrese el nombre del curso")

#########elimina curso#############

@login_required
def elimina_curso(request , id ):
    curso = Curso.objects.get(id=id)
    curso.delete()
    curso = Curso.objects.all()
    return render(request , "cursos.html" , {"cursos":curso})


#########editar curso#############

@login_required
def editar_curso(request , id):
    curso = Curso.objects.get(id=id)
    if request.method == "POST":
        mi_formulario = Curso_formulario( request.POST )
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            curso.nombre = datos["nombre"]
            curso.camada = datos["camada"]
            curso.save()
            curso = Curso.objects.all()
        return render(request , "cursos.html" , {"cursos":curso})
       
    else:
           mi_formulario = Curso_formulario(initial={"nombre":curso.nombre , "camada":curso.camada})
           avatares = Avatar.objects.filter(user=request.user.id) 
    return render( request , "editar_curso.html" , {"mi_formulario": mi_formulario , "curso":curso, 'url': avatares[0].imagen.url if avatares.exists() else None})

############################################
###################profesor#################
############################################
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
    avatares = Avatar.objects.filter(user=request.user.id) 
    return render(request, "formulario_profesores.html", {'url': avatares[0].imagen.url if avatares.exists() else None})
         

############ver profesores#############


def  ver_profesores(request):
     profesor = profesores.objects.all()
     avatares = Avatar.objects.filter(user=request.user.id)
     return render(request, 'profesores.html', {'profesores': profesor, 'url': avatares[0].imagen.url if avatares.exists() else None})
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

#########elimina profesor#############
@login_required
def elimina_profesor(request , id ):
    prof = profesores.objects.get(id=id)
    prof.delete()
    prof = profesores.objects.all()
    return render(request , "profesores.html" , {"profesores":prof})

###############editar profesor###########
@login_required
def editar_profesor(request , id):
    prof = profesores.objects.get(id=id)
    print(prof.nombre)
    print(prof.camada)
    if request.method == "POST":
        mi_formulario_pro = Profesor_formulario( request.POST )
        if mi_formulario_pro.is_valid():
            datos_pro = mi_formulario_pro.cleaned_data
            prof.nombre = datos_pro["nombre"]
            prof.camada = datos_pro["camada"]
            prof.save()
            prof = profesores.objects.all()
            return render(request , "profesores.html" , {"profesores":prof})
       
    else:
        mi_formulario_pro = Profesor_formulario(initial={"nombre":prof.nombre , "camada":prof.camada})
        avatares = Avatar.objects.filter(user=request.user.id) 
        return render(request,"editar_profesor.html" , {"mi_formulario_pro": mi_formulario_pro , "prof":prof, 'url': avatares[0].imagen.url if avatares.exists() else None})
  

############################################
#################alumnos################
############################################

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
    avatares = Avatar.objects.filter(user=request.user.id) 
    return render(request, "formulario_alumnos.html", {'url': avatares[0].imagen.url if avatares.exists() else None})


def ver_alumnos(request):
    alumnos = Alumnos.objects.all()  # Suponiendo que Alumno es el modelo de tu tabla de alumnos
    avatares = Avatar.objects.filter(user=request.user.id)
    return render(request, 'alumnos.html', {"alumnos": alumnos, 'url': avatares[0].imagen.url if avatares.exists() else None})

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

##########eliminar alumno##############
@login_required
def elimina_alumno(request , id ):
    alum = Alumnos.objects.get(id=id)
    alum.delete()
    alum = Alumnos.objects.all()
    return render(request , "alumnos.html" , {"alumnos":alum})

################edita alumno#########################
@login_required
def editar_alumno(request , id):
    alum = Alumnos.objects.get(id=id)
    if request.method == "POST":
        mi_formulario_alum = AlumnoForm( request.POST )
        if mi_formulario_alum.is_valid():
            datos_alu =  mi_formulario_alum.cleaned_data
            alum.nombre = datos_alu["nombre"]
            alum.dni = datos_alu["dni"]
            alum.save()
            alum = Alumnos.objects.all()
        return render(request , "alumnos.html" , {"alumnos":alum})
       
    else:
        mi_formulario_alum = AlumnoForm(initial={"nombre":alum.nombre , "dni":alum.dni})
        avatares = Avatar.objects.filter(user=request.user.id)
        return render(request,"editar_alumnos.html", {"mi_formulario_alum":mi_formulario_alum, "alum":alum, 'url': avatares[0].imagen.url if avatares.exists() else None})
       
   

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
                avatares = Avatar.objects.filter(user=request.user.id)
                return render( request , "inicio.html" , {"url":avatares[0].imagen.url})
            else:
                return HttpResponse(f"Usuario no encontrado")
        else:
            return HttpResponse(f"FORM INCORRECTO {form}")

    form = AuthenticationForm()
    return render( request , "login.html" , {"form":form})

    ###########registro##########


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')  # Obtener el nombre de usuario
            form.save()
            return render(request, "usuario_registrado.html", {'username': username})  # Pasar el nombre de usuario al template
    else:
        form = UserCreationForm()
    return render(request, "registro.html", {"form": form})

###############editar perfil#############
def editarPerfil(request):
    usuario = request.user
    if request.method == "POST":
        
        mi_formulario = UserEditForm(request.POST)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            usuario.email = informacion["email"]
            password = informacion["password1"]
            usuario.set_password(password)
            usuario.save()
            return render(request , "inicio.html")
    else:
        miFormulario = UserEditForm(initial={"email":usuario.email})
    
    return render( request , "editar_perfil.html", {"miFormulario":miFormulario, "usuario":usuario})
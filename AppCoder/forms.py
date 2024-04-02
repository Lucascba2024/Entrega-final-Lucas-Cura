from django import forms

class Curso_formulario(forms.Form):
      nombre = forms.CharField (max_length=30)
      camada = forms.IntegerField()

class Profesor_formulario(forms.Form):
      nombre = forms.CharField (max_length=30)
      camada = forms.IntegerField()

class AlumnoForm(forms.Form):
      nombre = forms.CharField (max_length=30)
      dni = forms.IntegerField()      
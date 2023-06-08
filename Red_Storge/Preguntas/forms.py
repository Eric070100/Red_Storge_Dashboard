from django import forms
from .models import Pregunta, Opcion, Contestacion

class FormPregunta(forms.ModelForm):
    class Meta:
        model = Pregunta
        fields = '__all__'
        widgets ={
            'id_pregunta' : forms.NumberInput(attrs={'class':'form-control','placeholder':'id_pregunta'}),
            'planteamiento' : forms.TextInput( attrs={'class':'form-control','placeholder':'Planteamiento'}),
            'modulo' : forms.Select( attrs={'class':'form-control','placeholder':'Modulo'}),
            'fase' : forms.Select( attrs={'class':'form-control','placeholder':'Fase'})
        }

class FormPreguntaEditar(FormPregunta):
    class Meta:
        exclude = ['id_pregunta']
        model = Pregunta

class FormOpcion(forms.ModelForm):
    class Meta:
        model = Opcion
        fields = '__all__'
        widgets ={
            'id_opcion' : forms.NumberInput(attrs={'class':'form-control','placeholder':'id_opcion'}),
            'descripcion': forms.Textarea(attrs={'rows': 3}),
        }

class FormOpcionEditar(FormOpcion):
    class Meta:
        exclude = ['id_opcion']
        model = Opcion

class FormContestacion(forms.ModelForm):
    class Meta:
        model = Contestacion
        fields = '__all__'
        widgets ={
            
        }

class FormContestacionEditar(FormContestacion):
    class Meta:
        exclude = ['id_contestacion']
        model = Contestacion
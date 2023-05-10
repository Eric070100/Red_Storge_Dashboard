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
        }

class FormPreguntaEditar(FormPregunta):
    class Meta:
        exclude = ['id_pregunta']
        model = Pregunta
from django import forms
from .models import Plantel, Grupo


class FormPlantel(forms.ModelForm):
    class Meta:
        model = Plantel
        fields = '__all__'
        widgets ={
            'id_plantel' : forms.NumberInput(attrs={'class':'form-control','placeholder':'id_plantel'}),
            'nombre_plantel' : forms.TextInput( attrs={'class':'form-control','placeholder':'Nombre'}),
            'domicilio' : forms.TextInput( attrs={'class':'form-control','placeholder':'Domicilio'}),
            'numero_telefono': forms.TextInput( attrs={'class':'form-control','placeholder':'Telefono'}),
        }
class FormGrupo(forms.ModelForm):
    class Meta:
        model = Grupo
        fields = '__all__'
        widgets = {
            'id_grupo' : forms.NumberInput(attrs={'class':'form-control','placeholder':'id_grupo'}),
            'grado' : forms.NumberInput(attrs={'class':'form-control','placeholder':'Grado'}),
            'letra' : forms.TextInput( attrs={'class':'form-control','placeholder':'Letra'}),
            'id_plantel' : forms.Select(attrs={'class':'form-control','placeholder':'Plantel'})
        }

class FormGrupoEditar(FormGrupo):
    class Meta:
        exclude = ['id_grupo']
        model = Grupo

class FormPlantelEditar(FormPlantel):
    class Meta:
        exclude = ['id_plantel']
        model = Plantel
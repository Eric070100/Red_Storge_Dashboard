from django import forms
from .models import Estudiante, Encargo_plantel
from django.contrib.auth.models import User

class FormEstudiante(forms.ModelForm):
    
    class Meta:
        model = Estudiante
        exclude = ['usuario']
        widgets = {
            'fecha_nacimiento': forms.DateInput(
                attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control'}
            )
        }
       
        
class FormEP(forms.ModelForm):
    
    class Meta:
        model = Encargo_plantel
        exclude = ['usuario']
        widgets = {
            'fecha_nacimiento': forms.DateInput(
                attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control'}
            )
        }

class UserForm(forms.ModelForm):
    re_pass = forms.CharField(
        label='Confirma contraseña',
        widget=forms.PasswordInput(),
        required=True
    )
    
    password = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(),
        required=True
    )
    class Meta:
        model = User
        fields = ['username','email','password','re_pass']
        # fields = '__all__'

    def clean_password(self, *args, **kwargs):
        if self.data['password'] != self.data['re_pass']:
            raise forms.ValidationError('Las contraseñas no son iguales', code='passwords_not_equals')
        return self.data['password']
    
    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
    



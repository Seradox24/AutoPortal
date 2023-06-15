from django.db import models
from django import forms
from django.forms import ModelForm, PasswordInput


class Formulario_Login(forms.Form):
    correo = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'E-Mail', 'autocomplete': 'new-password'}))
    password = forms.CharField(widget=PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña', 'autocomplete': 'new-password'}))


class Formulario_Registro(forms.Form):
    nombre = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control aaaaa', 'placeholder': 'Nombre', 'autocomplete':'off'}))
    apellido = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido', 'autocomplete':'off'}))
    correo = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'E-Mail', 'autocomplete': 'new-password'}))
    password = forms.CharField(widget=PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña', 'autocomplete': 'new-password'}))
    password2 = forms.CharField(widget=PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Repetir Contraseña', 'autocomplete': 'new-password'}))
def __init__(self, *args, **kwargs):
        super(Formulario_Registro, self).__init__(*args, **kwargs)
        self.fields['correo'].widget.attrs['autocomplete'] = 'new-password'
        self.fields['password'].widget.attrs['autocomplete'] = 'new-password'
        for field_name, field in self.fields.items():
            field.widget.attrs['autocomplete'] = 'off'


class Formulario_Reset(forms.Form):
    correo = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'E-Mail', 'autocomplete':'off'}))


class Formulario_Restore(forms.Form):
    password1 = forms.CharField(widget=PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}))
    password2 = forms.CharField(widget=PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Repetir Contraseña'}))

def __init__(self, *args, **kwargs):
        super(Formulario_Login, self).__init__(*args, **kwargs)
        self.fields['correo'].widget.attrs['autocomplete'] = 'new-password'
        self.fields['password'].widget.attrs['autocomplete'] = 'new-password'
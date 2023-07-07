from home.models import Vehiculo, Producto , ProductoCategoria, Proveedor, Estado, Sucursal, ProductoFotos, UsersMetadata, Perfiles, Documento,OrdenDeCompra 
from django import forms
from utilidades.dreamhost import moverArchivoProductoGaleria
from utilidades import formularios

from django.contrib.auth.models import User

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = ('numero_articulo','condicion', 'tipo_vehiculo', 'marca', 'modelo', 'volumen_motor', 'volante', 'transmision', 'tipo_combustible', 'puertas', 'color_exterior','num_pasajeros','num_vin','costo_reserva')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['condicion'].widget = forms.Select(choices=self.get_condicion_choices())
        self.fields['volumen_motor'].widget = forms.Select(choices=self.get_volumen_motor_choices())
        self.fields['volante'].widget = forms.Select(choices=self.get_volante_choices())
        self.fields['transmision'].widget = forms.Select(choices=self.get_transmision_choices())
        self.fields['tipo_combustible'].widget = forms.Select(choices=self.get_tipo_combustible_choices())
        self.fields['puertas'].widget = forms.Select(choices=self.get_puertas_choices())
        self.fields['color_exterior'].widget = forms.Select(choices=self.get_color_exterior_choices())

        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

    def get_condicion_choices(self):
        opciones_condicion = Vehiculo.CONDICION_CHOICES
        choices = [(opcion[0], opcion[1]) for opcion in opciones_condicion]
        return choices

    def get_volumen_motor_choices(self):
        opciones_volumen_motor = Vehiculo.VOLUMEN_MOTOR_CHOICES
        choices = [(opcion[0], opcion[1]) for opcion in opciones_volumen_motor]
        return choices

    def get_volante_choices(self):
        opciones_volante = Vehiculo.TIPO_VOLANTE
        choices = [(opcion[0], opcion[1]) for opcion in opciones_volante]
        return choices

    def get_transmision_choices(self):
        opciones_transmision = Vehiculo.TIPO_TRANSMISION
        choices = [(opcion[0], opcion[1]) for opcion in opciones_transmision]
        return choices

    def get_tipo_combustible_choices(self):
        opciones_tipo_combustible = Vehiculo.TIPO_COMBUSTIBLE
        choices = [(opcion[0], opcion[1]) for opcion in opciones_tipo_combustible]
        return choices

    def get_puertas_choices(self):
        opciones_puertas = Vehiculo.PUERTAS_CHOICES
        choices = [(opcion[0], opcion[1]) for opcion in opciones_puertas]
        return choices

    def get_color_exterior_choices(self):
        opciones_color_exterior = Vehiculo.COLOR_EXTERIOR_CHOICES
        choices = [(opcion[0], opcion[1]) for opcion in opciones_color_exterior]
        return choices




class Formulario_producto(forms.Form):
    nombre = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre', 'autocomplete':'off'}))
    titulo = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título', 'autocomplete':'off'}))
    descripcion = forms.CharField(required=True, widget=forms.Textarea(attrs={'rows': 3, 'cols': 100, 'class': 'form-control', 'placeholder': 'Descripción', 'id': 'mensaje', 'autocomplete':'off'}))
    adiccional = forms.CharField(required=True, widget=forms.Textarea(attrs={'rows': 3, 'cols': 100, 'class': 'form-control', 'placeholder': 'Adicional', 'id': 'adicional', 'autocomplete':'off'}))
    producto_categoria = forms.ChoiceField(required=True, widget=forms.Select(attrs={'class': 'form-control'}))
    proveedor = forms.ChoiceField(required=True, widget=forms.Select(attrs={'class': 'form-control'}))
    estado = forms.ChoiceField(required=True, widget=forms.Select(attrs={'class': 'form-control'}))
    sucursal = forms.ChoiceField(required=True, widget=forms.Select(attrs={'class': 'form-control'}))
    precio = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Precio', 'onkeypress': 'return soloNumeros(event)', 'autocomplete':'off'}))
    file = forms.CharField(required=False, widget=forms.TextInput(attrs={ 'type': 'file', 'id':'formFile', 'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['producto_categoria'].widget.choices = self.get_producto_categoria_choices()
        self.fields['proveedor'].widget.choices = self.get_proveedor_choices()
        self.fields['estado'].widget.choices = self.get_estado_choices()
        self.fields['sucursal'].widget.choices = self.get_sucursal_choices()
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

    def get_producto_categoria_choices(self):
        opciones_categoria = ProductoCategoria.objects.all()
        choices = [(opcion.id, opcion.nombre) for opcion in opciones_categoria]
        return choices

    def get_proveedor_choices(self):
        opciones_proveedor = Proveedor.objects.all()
        choices = [(opcion.id, opcion.nombre) for opcion in opciones_proveedor]
        return choices

    def get_estado_choices(self):
        opciones_estado = Estado.objects.all()
        choices = [(opcion.id, opcion.nombre) for opcion in opciones_estado]
        return choices

    def get_sucursal_choices(self):
        opciones_sucursal = Sucursal.objects.all()
        choices = [(opcion.id, opcion.nombre) for opcion in opciones_sucursal]
        return choices


from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User




class EditarUsuarioForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop('password')
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'


 

class UsersMetadataForm(forms.ModelForm):
    class Meta:
        model = UsersMetadata
        exclude = ('foto', 'estado', 'perfiles', 'slug', 'correo','user')
        widgets = {
            
            'genero': forms.Select(attrs={'class': 'form-control'}),
            'pais': forms.Select(attrs={'class': 'form-control'}),
            'comuna': forms.Select(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
        }



class DocumentoForm(forms.ModelForm):
    ordenDeCompra_id = forms.ModelChoiceField(queryset=OrdenDeCompra.objects.none(), widget=forms.Select(attrs={'class': 'form-control'}))
    nombre = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    descripcion = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    archivo = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Documento
        fields = ['nombre', 'descripcion', 'archivo']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            users_metadata_id = UsersMetadata.objects.get(user=user).id
            self.fields['ordenDeCompra_id'].queryset = OrdenDeCompra.objects.filter(users_metadata_id=users_metadata_id)

    def save(self, commit=True, request=None):
        documento = super().save(commit=False)
        documento.ordenDeCompra_id = self.cleaned_data['ordenDeCompra_id'].id
        documento.estado_id = 3  # Valor predeterminado para estado_id

        users_metadata = UsersMetadata.objects.get(user=request.user)
        documento.users_metadata_id = users_metadata.id

        if commit:
            documento.save()

        return documento










   
        
        

    
        
      
        
        
       
        
        
        
        
           
        






from django import forms
from django.forms import ModelForm

from .models import usuario, cliente, factura, venta, producto, categoria, carrito_producto, administrador, reserva

#!!!MARCO, hay algunos forms que le cambie la forma como les mostre en llamada, si quieres usar un form de los que no 
#! modifique, te recomendaria que los uses como la segunda forma que hice

#CORRECIONES, CAMBIE A USUARIOS EN LUGAR DE USUARIO DE LOS FORMS Y CORREGI forms.Forms de algunos

class CrearUsuario(forms.Form):  #!No tiene vistas
    nombre = forms.CharField(label="Ingrese el nombre del usuario", max_length=50)
    apellido = forms.CharField(label="Ingrese el apellido del usuario", max_length=50)
    direccion = forms.CharField(label="Ingrese la direccion del usuario", max_length=50)
    celular = forms.IntegerField(label="Ingrese el celular del usuario")
    correo = forms.EmailField(label="Ingrese el correo del usuario", max_length=50)
    password = forms.CharField(label="Ingrese la contraseña del usuario", max_length=50, widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirme la contraseña", max_length=50, widget=forms.PasswordInput)

# class CrearAdministrador(forms.Form):
#     usuarios_id_usuario_id = forms.IntegerField(label=
#     "Ingrese el id del usuario de este administrador") #?

# class CrearUsuario(ModelForm):  #!No tiene vistas
#     password=forms.CharField(widget=forms.PasswordInput) #ahora es contrasenia el campo
#     class Meta:
#         model = usuario
#         fields=['nombre', 'apellido', 'direccion','celular','correo','password']

class CrearAdministrador(ModelForm):
    class Meta:
        model = administrador
        fields=['usuarios_id_usuario']


class CrearReservas(forms.Form):  
    precio = forms.DecimalField(label="Ingrese el precio", max_digits=5, decimal_places=2)
    fecha = forms.DateField(label="Ingrese la fecha de la reserva")
    cantidad = forms.IntegerField(label="Ingrese la cantidad de productos de la reserva")
    penalizacion_id_penalizacion_id = forms.IntegerField(label=
    "Ingrese el id de la penalizacion correspondiente") #?

# class alterVenta(ModelForm):
#     class Meta: #En cual modelo estara basado
#         model = venta
#         fields=['id', 'fecha', 'administrador', 'productos', 'forma_de_pago', 'confirmada']

class CrearPenalizacion(forms.Form):  
    tipo_penalizacion = forms.CharField(label=
    "Ingrese el nombre de la penalizacion", max_length=50)
    monto = forms.DecimalField(label=
    "Ingrese monto correspondiente de la penalizacion", max_digits=5, decimal_places=2)


#ALE

# class CrearUsuario(forms.Form):
#     nombre = forms.CharField(max_length=50)
#     apellido = forms.CharField(max_length=50)
#     direccion = forms.CharField(max_length=50)
#     celular = forms.IntegerField()
#     correo = forms.CharField(max_length=30)
#     password = forms.CharField(max_length=40)

class CrearCliente(forms.Form):
    NIT = forms.CharField(label="NIT", max_length=15, widget=forms.TextInput(attrs={'class':'input'}))
    id_usuario = forms.ModelChoiceField(queryset=usuario.objects.all(), widget=forms.Select(attrs={'class':'input'}))
    #TODO: crear usuario del cliente

class CrearFactura(forms.Form):
    fecha = forms.DateField(label="Fecha", widget=forms.DateInput(attrs={'class':'input'}))
    forma_de_pago = forms.CharField(label="Forma de pago", max_length=20, widget=forms.TextInput(attrs={'class':'input'}))
    razon_social = forms.CharField(label="Razon social", max_length=50, widget=forms.TextInput(attrs={'class':'input'}))
    telefono = forms.CharField(label="Telefono", max_length=15, widget=forms.TextInput(attrs={'class':'input'}))
    correo = forms.CharField(label="Correo", max_length=50, widget=forms.TextInput(attrs={'class':'input'}))
    subtotal = forms.DecimalField(label="Subtotal", max_digits=10, decimal_places=2, widget=forms.TextInput(attrs={'class':'input'}))
    IVA = forms.DecimalField(label="IVA", max_digits=10, decimal_places=2, widget=forms.TextInput(attrs={'class':'input'}))

class CrearVenta(forms.Form):
    fecha = forms.DateField(label="Fecha", widget=forms.DateInput(attrs={'class':'input'}))
    administrador_ci = forms.IntegerField(label="Administrador", widget=forms.TextInput(attrs={'class':'input'}))
    cliente_NIT = forms.CharField(label="NIT", max_length=15, widget=forms.TextInput(attrs={'class':'input'}))
    producto_codigo = forms.IntegerField(label="Codigo", widget=forms.TextInput(attrs={'class':'input'}))
    reservas_num = forms.IntegerField(label="Reserva", widget=forms.TextInput(attrs={'class':'input'}))

class CrearFacturaVenta(forms.Form):
    id_factura = forms.IntegerField(label="ID factura", widget=forms.TextInput(attrs={'class':'input'}))
    id_venta = forms.IntegerField(label="ID venta", widget=forms.TextInput(attrs={'class':'input'}))

#MARCO

class NewCarrito(forms.Form):
    fecha = forms.DateField(label="Fecha")
    total = forms.DecimalField(label="Total",max_digits=5,decimal_places=2)
    cantidad = forms.IntegerField(label="Cantidad")
    cliente_nit = forms.ModelChoiceField(queryset=cliente.objects.all(), widget=forms.Select(attrs={'class':'input'}))
    productos_id_productos = forms.ModelChoiceField(queryset=producto.objects.all(), widget=forms.Select(attrs={'class':'input'}))

# class NewProducto(forms.Form):
#     nombre = forms.CharField(label="Nombre", max_length=30)
#     precio = forms.DecimalField(label="Precio",max_digits=5,decimal_places=2)
#     descripcion = forms.CharField(label="Descripcion",widget=forms.Textarea,max_length=100)
#     disponible = forms.BooleanField(label="En stock")
#     marca = forms.CharField(label="Marca",max_length=20)
#     cantidad = forms.IntegerField(label="Cantidad")
#     categoria_id_categoria = forms.ModelChoiceField(queryset=categoria.objects.all(), widget=forms.Select(attrs={'class':'input'}))


class CrearCategoria(ModelForm):
    descripcion = forms.CharField(widget=forms.Textarea)
    class Meta: #En cual modelo estara basado
        model = categoria
        fields=['nombre', 'descripcion']

class CrearProducto(ModelForm):
    descripcion = forms.CharField(widget=forms.Textarea)
    class Meta: #En cual modelo estara basado
        model = producto
        fields=['nombre', 'precio', 'descripcion','disponible','marca','stock','categoria_id_categoria','img']
class NewProducto(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=30)
    precio = forms.DecimalField(label="Precio",max_digits=5,decimal_places=2)
    descripcion = forms.CharField(label="Descripcion",widget=forms.Textarea,max_length=100)
    disponible = forms.BooleanField(label="En stock")
    marca = forms.CharField(label="Marca",max_length=20)
    stock = forms.IntegerField(label="stock")
    categoria_id_categoria = forms.ModelChoiceField(queryset=categoria.objects.all(), widget=forms.Select(attrs={'class':'input'}))
    img = forms.ImageField(label="Imagen")


class NewCarrito_producto(ModelForm):
    class Meta: #En cual modelo estara basado
        model = carrito_producto
        fields=['carrito', 'producto', 'cantidad']

# class CrearReserva(ModelForm):
#     class Meta: #En cual modelo estara basado
#         model = venta
#         fields=['precio','fecha','venta','penalizacion_id_penalizacion']


#   ALE

class AddToCartForm(forms.Form):
    quantity = forms.IntegerField(label="Cantidad", min_value=0, max_value=10, widget=forms.NumberInput(attrs={'class':'input'}))

class HacerVenta(forms.Form):
    CHOICES = [('tarjeta','tarjeta'),('efectivo','efectivo')]
    payment = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
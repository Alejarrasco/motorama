from django.db import models

# Create your models here.
class usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    celular = models.IntegerField()
    correo = models.EmailField(max_length=30) #ahora es correo
    password = models.CharField(max_length=40)
    def __str__(self):
            return "id:"+ str(self.pk) + " Nombre:" + self.nombre

class cliente(models.Model):
    NIT = models.CharField(max_length=15, primary_key=True)
    id_usuario = models.ForeignKey(usuario, on_delete=models.CASCADE)

class administrador(models.Model):
    usuarios_id_usuario = models.ForeignKey(usuario, on_delete=models.CASCADE)
    def __str__(self):
            return self.usuarios_id_usuario.nombre

class categoria(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    
    def __str__(self):
            return "id:"+ str(self.pk) + " Nombre:" + self.nombre

class producto(models.Model):
    nombre = models.CharField(max_length=30)
    precio = models.DecimalField(max_digits=7, decimal_places=2)
    descripcion = models.CharField(max_length=100)
    disponible = models.BooleanField()
    marca = models.CharField(max_length=20)
    stock = models.IntegerField()
    categoria_id_categoria = models.ForeignKey(categoria, on_delete=models.CASCADE)
    def __str__(self): #to string
        return "id:" +str(self.pk) + "nombre:" +self.nombre + '- cateogoria_id_categoria ' + str(self.categoria_id_categoria) #creo que lo referencia en base al fk

class penalizacion(models.Model):
    tipo_penalizacion = models.CharField(max_length=50, blank=True)
    monto = models.DecimalField(max_digits=7, decimal_places=2)
    def __str__(self):
                return "id:"+ str(self.pk)

class carrito(models.Model):
    cliente = models.ForeignKey(cliente, on_delete=models.CASCADE)
    activo = models.BooleanField()
    def __str__(self):
                return str(self.pk)

    def total(self):
        return sum(item.subtotal() for item in carrito_producto.objects.filter(carrito=self.pk))

class carrito_producto(models.Model):
    carrito = models.ForeignKey(carrito, on_delete=models.CASCADE)
    producto = models.ForeignKey(producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

    def subtotal(self):
        return self.cantidad * self.producto.precio

class venta(models.Model):
    fecha = models.DateField()
    administrador = models.ForeignKey(administrador, on_delete=models.CASCADE)
    productos = models.ForeignKey(carrito, on_delete=models.CASCADE)
    forma_de_pago = models.CharField(max_length=20, default='efectivo')
    estado=models.CharField(max_length=1, default='p')
    def __str__(self):
                return "id:"+ str(self.pk)

class reserva(models.Model):
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateField()
    venta = models.ForeignKey(venta, on_delete=models.CASCADE)
    penalizacion_id_penalizacion = models.ForeignKey(penalizacion, on_delete=models.CASCADE)
    
    def __str__(self):
            return "id:"+ str(self.pk)

class factura(models.Model):
    fecha = models.DateField()
    forma_de_pago = models.CharField(max_length=20)
    razon_social = models.CharField(max_length=50)
    telefono = models.CharField(max_length=15)
    correo = models.CharField(max_length=50)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    IVA = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    venta_id_venta = models.ForeignKey(venta, on_delete=models.CASCADE)
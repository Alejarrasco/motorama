from django.contrib import admin
from .models import categoria, cliente, producto, usuario, administrador, penalizacion, carrito, carrito_producto, venta, reserva, factura

# Register your models here.
admin.site.register(categoria)
admin.site.register(cliente)
admin.site.register(producto)
admin.site.register(usuario)
admin.site.register(administrador)
admin.site.register(penalizacion)
admin.site.register(carrito)
admin.site.register(carrito_producto)
admin.site.register(venta)
admin.site.register(reserva)
admin.site.register(factura)

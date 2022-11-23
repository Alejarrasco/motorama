#ALE
from datetime import datetime
from django.shortcuts import get_object_or_404, render, redirect
from .models import producto, cliente, carrito, usuario, carrito_producto, venta, administrador, factura
from .forms import AddToCartForm
from .utils import numero_to_letras
from django.contrib import messages

#YO
from django.shortcuts import render, redirect, get_object_or_404
from .models import usuario, administrador, reserva, penalizacion, producto, categoria
from .forms import CrearAdministrador, CrearReservas, CrearPenalizacion, CrearUsuario, CrearProducto, CrearCategoria
from django.forms import formset_factory, modelformset_factory, inlineformset_factory
from django.contrib.auth import login, logout, authenticate
#from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.utils import timezone #diferente al de python
#MARCO
import numpy as np

# Create your views here.

def index(request):
    return render(request, 'index.html', {})

def registroUsuario(request):
    if request.method=='POST':
        nombre=request.POST['Nombre']
        apellido = request.POST['Apellido']
        direccion = request.POST['Direccion']
        celular = request.POST['Celular']
        nit = request.POST['NIT']
        correo = request.POST['Correo']
        password = request.POST['Password']
        u = usuario(nombre=nombre,apellido=apellido,direccion=direccion,celular=celular,correo=correo,password=password)
        u.save()
        cliente.objects.create(NIT=nit,id_usuario=u)
        carrito.objects.create(cliente=cliente.objects.get(NIT=nit), activo=True)
        
        messages.success(request,'El usuario '+request.POST['Nombre']+' se ha registrado exitosamente')
        return render(request,'login/signUp.html')
    else:
        return render(request,'login/signUp.html')

def paginaLogin(request):
    if request.method=='POST':
        try:
            detalleUsuario=usuario.objects.get(correo=request.POST['Correo'],password=request.POST['Password'])
            return render(request, 'InterfazCliente\home.html', {'usuario': detalleUsuario,
                                                         'cliente': cliente.objects.get(id_usuario=detalleUsuario)})
        except usuario.DoesNotExist as e:
            messages.success(request,'Nombre de Usuario o Password incorrecto!')
    return render(request,'login/Log_In.html')

#     def sign_Up(request):
#         return render(request, 'login/signUp.html')

#     def logIn(request):
#         if request.method == 'GET':
#             return render(request, 'login/logIn.html')
#         else:
#             print(request.POST)
#             user=usuario.objects.filter(correo=request.POST['correo'], password=request.POST['password'])
#             if(user):
#                 print("xd")
#                 print(user)
#                 #login(request, user)
#                 return redirect('index')
#             #user=authenticate(request, usuario.nombre=request.POST['username'], password=request.POST['password'])
#             else:
#                 return render(request, 'login/logIn.html',{
#                     'error' : 'No existe este usuario'
#                 })  

def homeadmin(request, aid):
    adminActivo = get_object_or_404(administrador, id=aid)
    return render(request, 'InterfazAdmin\home.html', {'admin': adminActivo})      

def leerAdministradores(request):
    #projects = list(Project.objects.values()) #lista de proyectos en query set
    administradores=administrador.objects.all() 
    return render(request,'InterfazAdmin/leerAdministradores.html',{
        'administradores':administradores
    })

def crearAdministradores(request): #este es el secundario, principalmente es con crear usuario
    if request.method == 'GET':
        #show interface
        return render(request,'InterfazAdmin/create_administradores.html',{
        'form':CrearAdministrador 
        })        
    else:
        administrador.objects.create(usuarios_id_usuario_id=request.POST["usuarios_id_usuario_id"])
        return redirect('index')

# def leerReservas(request):
#     return render(request,'InterfazAdmin/reservas.html')
#     # if request.method == 'GET':
#     #     #show interface
#     #     return render(request,'projects/create_project.html',{
#     #     'form':CrearReservas 
#     #     })        
#     # else:
#     #     reserva.objects.create(precio=request.POST["precio"], fecha=request.POST["fecha"],
#     #     cantidad=request.POST["cantidad"], penalizacion_id_penalizacion_id=request.POST["penalizacion_id_penalizacion_id=request"])
#     #     return redirect('index')

def leerPenalizaciones(request):
    if request.method == 'GET':
        #show interface
        return render(request,'projects/create_project.html',{
        'form':CrearPenalizacion 
        })        
    else:
        penalizacion.objects.create(tipo_penalizacion=request.POST["tipo_penalizacion"]
        , monto=request.POST["monto"])
        return redirect('index')

def leerProductos(request):
    #projects = list(Project.objects.values()) #lista de proyectos en query set
    #productos=producto.objects.all() 
    productos = producto.objects.all()
    categorias = categoria.objects.all()
    try:
        return render(request,'InterfazAdmin/leerProductos.html',{
            'productos':productos,
            'categorias' : categorias
        })
    except:
        return render(request,'InterfazAdmin/leerProductos.html',{
            'productos':productos,
            'error' : 'No hay productos'
        })



def CrearProductos(request):
    if request.method == 'GET':
        #show interface
        return render(request,'InterfazAdmin/create_product.html',{
        'form': CrearProducto
        })        
    else:
        try:
            form = CrearProducto(request.POST) #esto se quedara con el form en html parece
            form.save()
            #new_task.save()
            #producto.objects.create(form)    
            return redirect('leerProductos')
        except ValueError:
            return render(request, 'InterfazAdmin/create_product.html',{
            'form' : CrearProducto,
            'error' : 'Please provide valid data'
            })


def administrarProducto(request):
    productosFormset=modelformset_factory(producto, form=CrearProducto, can_delete=True)
    if request.method == 'POST':
        form = productosFormset(request.POST)
        print(request.POST)
        #print(request.POST)
        form.save()
        return redirect('leerProductos')
    form = productosFormset()
    return render(request, 'InterfazAdmin/administrarProductos.html', {
        'forms' : form
    })

def product_detail(request, producto_id):
    if request.method == 'GET':
        #task=Task.objects.get(pk=task_id) #asi obtenermos un dato en base a lo ingresado por referencia
        productos = get_object_or_404(producto, pk=producto_id) #del modelo task buscara el id
        form=CrearProducto(instance=productos) #llena el form con la tarea
        return render(request, 'InterfazAdmin/product_detail.html',{
            'productos' : productos,
            'form' : form
        })
    else:
        try:
                                                        #solo para aquellos donde coincide la tarea con el usuario creador y con sesion iniciada
            productos = get_object_or_404(producto, pk=producto_id) #del modelo task buscara el id
            form=CrearProducto(request.POST, instance=productos) #obtiene todo lo que haya en los forms y guarda el nuevo form
            form.save()
            #pass parece que sirve para continuar a traves de un error
            return redirect('leerProductos')
        except ValueError:
            return render(request, 'InterfazAdmin/product_detail.html',{
            'productos' : productos,
            'form' : form,
            'error' : 'Error actualizando producto'
        })

def eliminarProducto(request, producto_id):
    productos=get_object_or_404(producto, pk=producto_id)
    if request.method == 'POST':
        productos.delete()
        return redirect('leerProductos')

def CrearUsuarios(request):
    if request.method == 'GET':
        #show interface
        return render(request,'InterfazAdmin/create_usuario.html',{
        'form': CrearUsuario
        })        
    else:
        try:
            form = CrearUsuario(request.POST) #esto se quedara con el form en html parece
            new_task = form.save()
            id_user = get_object_or_404(usuario, nombre=request.POST['nombre'], apellido=request.POST['apellido'], direccion=request.POST['direccion'], celular=request.POST['celular'], correo=request.POST['correo'], password=request.POST['password'])
            administrador.objects.create(usuarios_id_usuario=id_user)
            #new_task.save()
            #producto.objects.create(form)    
            return redirect('leerUsuarios')
        except ValueError:
            return render(request, 'InterfazAdmin/create_usuario.html',{
            'form' : CrearUsuario,
            'error' : 'Please provide valid data'
            })

def leerUsuarios(request):
    #projects = list(Project.objects.values()) #lista de proyectos en query set
    #productos=producto.objects.all() 
    usuarios = usuario.objects.all()
    try:
        return render(request,'InterfazAdmin/leerUsuarios.html',{
            'usuarios':usuarios,
        })
    except:
        return render(request,'InterfazAdmin/leerUsuarios.html',{
            'usuarios':usuarios,
            'error' : 'No hay productos'
        })

def CrearCategorias(request):
    if request.method == 'GET':
        #show interface
        return render(request,'InterfazAdmin/create_categorias.html',{
        'form': CrearCategoria
        })        
    else:
        try:
            form = CrearCategoria(request.POST) #esto se quedara con el form en html parece
            form.save()
            return redirect('leerCategorias')
        except ValueError:
            return render(request, 'InterfazAdmin/create_categorias.html',{
            'form' : CrearCategoria,
            'error' : 'Porfavor, llene los campos con datos validos'
            })


def leerCategorias(request):
    categorias = categoria.objects.all()
    try:
        return render(request,'InterfazAdmin/leerCategorias.html',{
            'categorias':categorias,
        })
    except:
        return render(request,'InterfazAdmin/leerCategorias.html',{
            'categorias':categorias,
            'error' : 'No hay categorias'
        })

def leerReservas(request): #idea, haz que cuando estes en la pestania reserva puedas presionar detalle para asi ver todos los productos
    ventas = venta.objects.all()
    #print(ventas)
    # reservas= reserva.objects.all()
    # #print(reservas)
    # carritos = list(venta.objects.filter(estado='p').values('productos_id'))
    # print(carritos)
    # car_ids=[]
    # for car in carritos:
    #     for i in car.values():
    #         print(i)
    #         car_ids.append(i)
    # print(car_ids)
    # dets=[]
    # for det in range(len(car_ids)):
    #     #dets[det] = detalleReserva(request, car_ids[det])
    #     dets.append(detalleReserva(request, car_ids[det]))
    #     dets.append(car_ids[det])
    # print("detalle")
    # print(dets)
    # # for i in range(len(dets)):
    #     print(dets[i]+"\n")
    # detalle=detalleReserva(request, 12)
    return render(request,'InterfazAdmin/reservas2.html',{
            'reservas' : ventas,
        })

def leerReservasAceptadas(request): #idea, haz que cuando estes en la pestania reserva puedas presionar detalle para asi ver todos los productos
    ventas = venta.objects.filter(estado='a').order_by('-estado')
    #print(ventas)
    return render(request,'InterfazAdmin/reservasAcc.html',{
            'reservas' : ventas
        })


def aceptarReservas(request, venta_id):
    ventas=venta.objects.get(id=venta_id)
    ventas.estado='a'
    ventas.save()
    #penalizacion.objects.create(pk=venta_id, monto=0) #todo: cambialo, asignale no crees, como tarifario
    reserva.objects.create(pk=venta_id, precio=0, fecha=timezone.now(), venta_id=venta_id, penalizacion_id_penalizacion_id=1) #todo: cambialo
    return redirect('leerReservas')

def rechazarReservas(request, venta_id):
    ventas=venta.objects.get(id=venta_id)
    ventas.estado='r'
    ventas.save()
    return redirect('leerReservas')

def detalleReserva(request, carrito_id):
    productos=carrito_producto.objects.filter(carrito=carrito_id)
    total = carrito.objects.get(id=carrito_id).total()
    # det=""
    # for item in productos:
    #     det+="-"+item.producto.nombre+ " compro la cantidad de " +str(item.cantidad)
    #     det+="\n"
    print(productos)
    return render (request, 'InterfazAdmin/detalleReserva.html',{
        'carrito': carrito_id,
        'detalle' : productos,
        'total' : total,
    })


def detalleReservaAcc(request, carrito_id): #esto no se aun si quitar
    productos=carrito_producto.objects.filter(carrito=carrito_id)
    for item in productos:
        print(f"{item.producto.nombre} compro la cantidad de {item.cantidad}")
    return redirect('reservasAceptadas')

#           ALE


def home(request, cli):
    clienteActivo = get_object_or_404(cliente, NIT=cli)
    usuarioActivo = get_object_or_404(usuario, id=clienteActivo.id_usuario.id)
    return render(request, 'InterfazCliente\home.html', {'usuario': usuarioActivo,
                                                         'cliente': clienteActivo})

def about(request, cli):
    clienteActivo = get_object_or_404(cliente, NIT=cli)
    return render(request, 'InterfazCliente\\about.html', {'cliente': clienteActivo})

def productos(request, cli): #boton productos
    clienteActivo = get_object_or_404(cliente, NIT=cli)
    catalogo = producto.objects.all()
    return render(request, 'InterfazCliente\productos.html', {'cliente': clienteActivo,
                                                              'productos': catalogo})

def productDisplay(request, cli, pid): #aparece cuando seleccionas un producto
    clienteActivo = get_object_or_404(cliente, NIT=cli)
    productoActivo = get_object_or_404(producto, id=pid)
    if request.method == 'GET':
        return render(request, 'InterfazCliente\productoDisplay.html', {'cliente': clienteActivo,
                                                                        'producto': productoActivo,
                                                                        'form': AddToCartForm()})
    else:
        carritoActivo = get_object_or_404(carrito, cliente=clienteActivo, activo=True)
        carrito_producto.objects.create(carrito=carritoActivo, producto=producto.objects.get(id=pid), cantidad=request.POST['quantity'])
        return redirect('cart', cli=cli)

def cart(request, cli): #cuando presionas carrito
    clienteActivo = get_object_or_404(cliente, NIT=cli)
    carritoActivo = get_object_or_404(carrito, cliente=clienteActivo, activo=True)
    productos = carrito_producto.objects.filter(carrito=carritoActivo)

    subtotal = list()
    total = 0
    for item in productos:
        subtotal.append(item.producto.precio * item.cantidad)
        total += item.producto.precio * item.cantidad

    return render(request, 'InterfazCliente\carrito.html', {'cliente': clienteActivo,
                                                            'carrito': carritoActivo,
                                                            'productos': productos,
                                                            'subtotal': subtotal,
                                                            'total': total})

def confirmarVenta(request, cli):
    clienteActivo = get_object_or_404(cliente, NIT=cli)
    carritoActivo = get_object_or_404(carrito, cliente=clienteActivo, activo=True)
    productos = carrito_producto.objects.filter(carrito=carritoActivo)
    admins = list(administrador.objects.filter().values('pk'))
    ads=[]
    for admin in admins:
        for i in admin.values():
            print(i)
            ads.append(i)
    subtotal = list()
    total = 0
    for item in productos:
        subtotal.append(item.producto.precio * item.cantidad)
        total += item.producto.precio * item.cantidad


    if request.method == 'GET':
        return render(request, 'InterfazCliente\confirmarVenta.html', {'productos': productos,
                                                                        'subtotal': subtotal,
                                                                        'total': total,
                                                                        'cliente': clienteActivo})
    else:
        carritoActivo.activo = False
        carritoActivo.save()
        carrito.objects.create(cliente=carritoActivo.cliente, activo=True)


        venta.objects.create(fecha=datetime.now(), administrador=administrador.objects.get(id=np.random.choice(ads)), productos=carritoActivo, forma_de_pago=request.POST['pago'])

        return redirect('reservation', cli=carritoActivo.cliente.NIT, nvv=1)

def reservation(request, cli, nvv): #aparece cuando le das a save en carrito
    clienteActivo = get_object_or_404(cliente, NIT=cli)
    ventas = venta.objects.filter(productos__cliente=clienteActivo)
    for i in ventas:
        print(i.fecha)
        print(i.administrador)
    return render(request, 'InterfazCliente\\reserva.html', {'cliente': clienteActivo,
                                                            'ventas': ventas,
                                                            'nvv': nvv})

### factura
def facturar(request, res):
    ventaActiva = get_object_or_404(venta, id=res)
    fecha = datetime.now()
    forma_de_pago = ventaActiva.forma_de_pago
    razon_social = ventaActiva.productos.cliente.id_usuario.apellido
    telefono = ventaActiva.productos.cliente.id_usuario.celular
    correo = ventaActiva.productos.cliente.id_usuario.correo
    subtotal = ventaActiva.productos.total()
    iva = float(subtotal) * 0.13
    total = float(subtotal) + float(iva)
    f = factura(fecha=fecha, forma_de_pago=forma_de_pago, razon_social=razon_social, telefono=telefono, correo=correo, subtotal=subtotal, IVA=iva, total=total, venta_id_venta=ventaActiva)
    f.save()
    return printfactura(request, f.id)


def printfactura(request, nro):
    fact = get_object_or_404(factura, id=nro)
    detalle = carrito_producto.objects.filter(carrito=fact.venta_id_venta.productos)
    total_letras = numero_to_letras(fact.subtotal) + ' Bolivianos '
    valor = dict()
    for det in detalle:
        valor[det.producto.nombre] = det.cantidad * det.producto.precio
    return render(request, 'InterfazAdmin/factura.html', {'factura': fact, 'detalle': detalle, 'total_letras': total_letras, 'valor': valor})                                                            


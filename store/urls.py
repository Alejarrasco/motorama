#estas url es para estar mas organizado
from django.urls import path
from . import views #cuando pones . significa la ruta actual, osea importa de la ruta actual

urlpatterns=[
    # path('login/', views.login, name="login"), 

    path('', views.index, name="index"),


    #Interfaz Login
    path('signup/',views.registroUsuario,name='registro'),
    path('Log_In/',views.paginaLogin,name='paginaLogin'),
    path('Log_InAdmin/',views.paginaLoginAdmin,name='paginaLoginAdmin'),

    #Interfaz Administrador
    path('homeadmin/<int:aid>', views.homeadmin, name="homeadmin"), 
    path('leerAdministradores/<int:aid>', views.leerAdministradores, name="leerAdministradores"), 
    #path('crearAdministradores/', views.crearAdministradores, name="crearAdministradores"), 
    path('leerProductos/<int:aid>', views.leerProductos, name="leerProductos"), 
    path('leerProductos/<int:producto_id>/<int:aid>', views.product_detail,name='product_detail'),
    path('leerProductos/create/<int:aid>', views.CrearProductos, name="aniadir_producto"), 
    path('leerProductos/<int:producto_id>/delete/', views.eliminarProducto,name='eliminarProducto'),
    #path('admin_prod/', views.product_detail, name="admin_prod"), #quita esto
    path('leerReservas/<int:aid>', views.leerReservas, name="leerReservas"), 
    path('leerReservas/<int:venta_id>/aceptar/<int:aid>', views.aceptarReservas, name="aceptarReserva"), 
    path('leerReservas/<int:venta_id>/rechazar/<int:aid>', views.rechazarReservas, name="rechazarReserva"), 
    path('leerReservasAceptadas/<int:aid>', views.leerReservasAceptadas, name="reservasAceptadas"), 
    path('leerDetalleReserva/<int:carrito_id>/<int:aid>', views.detalleReserva, name="detalleReserva"), 
    path('leerDetalleReservaAcc/<int:carrito_id>/<int:aid>', views.detalleReservaAcc, name="detalleReservaAcc"), 
    #path('leerPenalizaciones/', views.leerPenalizaciones, name="leerPenalizaciones"),
    path('leerUsuarios/<int:aid>', views.leerUsuarios, name="leerUsuarios"),
    path('leerUsuarios/create/<int:aid>', views.CrearUsuarios, name="crearUsuarios"),
    #path('signup/', views.sign_Up, name="signup"),
    #path('login/', views.logIn, name="login"),
    path('leerCategorias/<int:aid>', views.leerCategorias, name="leerCategorias"),
    path('leerCategorias/create/<int:aid>', views.CrearCategorias, name="crearCategorias"),
    path('administrarProductos/<int:aid>', views.administrarProducto, name="administrarProductos"),
    
    #Interfaz Cliente
    #path('', views.index, name='index'),
    path('home/<int:cli>', views.home, name="home"),
    path('about/<int:cli>', views.about, name="about"),
    path('products/<int:cli>', views.productos, name="products"),
    path('productDisplay/<int:cli>/<int:pid>/', views.productDisplay, name="productDisplay"),
    #path('add_to_cart/<int:id>/', views.add_to_cart, name="add_to_cart"),
    path('cart/<int:cli>', views.cart, name="cart"),
    path('confirmSale/<int:cli>/', views.confirmarVenta, name="confirmSale"),
    path('reservation/<int:cli>/<int:nvv>', views.reservation, name="reservation"),
    path('reservation_Acpt/<int:cli>/<int:nvv>', views.reservationAcpt, name="reservation_Acpt"),
    path('facturar/<int:res>', views.facturar, name="facturar"),
    path('factura/<int:fac>', views.printfactura, name="factura"),
    path('eliminarProductoCarrito/<int:cli>/<int:ccp>', views.removeProductoCarrito, name='eliminarProductoCarrito'),
    path('verCarrito/<int:cli>/<int:ven>', views.verCarrito, name='spyCarrito')
    
]
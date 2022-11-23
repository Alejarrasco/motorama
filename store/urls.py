#estas url es para estar mas organizado
from django.urls import path
from . import views #cuando pones . significa la ruta actual, osea importa de la ruta actual

urlpatterns=[
    # path('login/', views.login, name="login"), 

    path('', views.index, name="index"),

    path('signUp/',views.registroUsuario,name='registro'),
    path('Log_In/',views.paginaLogin,name='paginaLogin'),

    path('homeadmin/<int:aid>', views.homeadmin, name="homeadmin"), 
    path('leerAdministradores/', views.leerAdministradores, name="leerAdministradores"), 
    #path('crearAdministradores/', views.crearAdministradores, name="crearAdministradores"), 
    path('leerProductos/', views.leerProductos, name="leerProductos"), 
    path('leerProductos/<int:producto_id>/', views.product_detail,name='product_detail'),
    path('leerProductos/create/', views.CrearProductos, name="aniadir_producto"), 
    path('leerProductos/<int:producto_id>/delete/', views.eliminarProducto,name='eliminarProducto'),
    #path('admin_prod/', views.product_detail, name="admin_prod"), #quita esto
    path('leerReservas/', views.leerReservas, name="leerReservas"), 
    path('leerReservas/<int:venta_id>/aceptar', views.aceptarReservas, name="aceptarReserva"), 
    path('leerReservas/<int:venta_id>/rechazar', views.rechazarReservas, name="rechazarReserva"), 
    path('leerReservasAceptadas/', views.leerReservasAceptadas, name="reservasAceptadas"), 
    path('leerDetalleReserva/<int:carrito_id>/', views.detalleReserva, name="detalleReserva"), 
    path('leerDetalleReservaAcc/<int:carrito_id>/', views.detalleReservaAcc, name="detalleReservaAcc"), 
    #path('leerPenalizaciones/', views.leerPenalizaciones, name="leerPenalizaciones"),
    path('leerUsuarios/', views.leerUsuarios, name="leerUsuarios"),
    path('leerUsuarios/create/', views.CrearUsuarios, name="crearUsuarios"),
    #path('signup/', views.sign_Up, name="signup"),
    #path('login/', views.logIn, name="login"),
    path('leerCategorias/', views.leerCategorias, name="leerCategorias"),
    path('leerCategorias/create/', views.CrearCategorias, name="crearCategorias"),
    path('administrarProductos/', views.administrarProducto, name="administrarProductos"),
    #!!!!ALE!!!!
    #path('', views.index, name='index'),
    path('home/<int:cli>', views.home, name="home"),
    path('about/<int:cli>', views.about, name="about"),
    path('products/<int:cli>', views.productos, name="products"),
    path('productDisplay/<int:cli>/<int:pid>/', views.productDisplay, name="productDisplay"),
    #path('add_to_cart/<int:id>/', views.add_to_cart, name="add_to_cart"),
    path('cart/<int:cli>', views.cart, name="cart"),
    path('confirmSale/<int:cli>/', views.confirmarVenta, name="confirmSale"),
    path('reservation/<int:cli>/<int:nvv>', views.reservation, name="reservation"),

    path('facturar/<int:res>', views.facturar, name="facturar"),
    path('factura/<int:fac>', views.printfactura, name="factura"),
    
]
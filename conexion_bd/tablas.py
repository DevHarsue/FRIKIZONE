from conexion_bd.objetos import *
from conexion_bd.tabla_hija import TablaHija

class TablaClientes(TablaHija):
    def __init__(self) -> None:
        self.nombre_tabla = "Clientes"
        self.claseFila = Cliente
        self.insertar_id = True
        super().__init__()
        
class TablaDivisas(TablaHija):
    def __init__(self) -> None:
        self.nombre_tabla = "Divisas"
        self.claseFila = Divisa
        self.insertar_id = False
        super().__init__()

class TablaMetodos(TablaHija):
    def __init__(self) -> None:
        self.nombre_tabla = "Metodos"
        self.claseFila = Metodo
        self.insertar_id = False
        super().__init__()
        
class TablaProductos(TablaHija):
    def __init__(self) -> None:
        self.nombre_tabla = "Productos"
        self.claseFila = Producto
        self.insertar_id = False
        super().__init__()

class TablaRoles(TablaHija):
    def __init__(self) -> None:
        self.nombre_tabla = "Roles"
        self.claseFila = Rol
        self.insertar_id = False
        super().__init__()

class TablaUsuarios(TablaHija):
    def __init__(self) -> None:
        self.nombre_tabla = "Usuarios"
        self.claseFila = Usuario
        self.insertar_id = True
        super().__init__()

class TablaVentas(TablaHija):
    def __init__(self) -> None:
        self.nombre_tabla = "Ventas"
        self.claseFila = Venta
        self.insertar_id = False
        super().__init__()

class TablaVentasDetalles(TablaHija):
    def __init__(self) -> None:
        self.nombre_tabla = "Ventas_Detalles"
        self.claseFila = VentaDetalle
        self.insertar_id = False
        super().__init__()
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
        
class TablaProductos(TablaHija):
    def __init__(self) -> None:
        self.nombre_tabla = "Productos"
        self.claseFila = Producto
        self.insertar_id = False
        super().__init__()
    
    def select_nombre(self,nombre):
        filas = self.bd.consultar(f"SELECT * FROM productos WHERE producto_nombre LIKE '{nombre}%'")
        filas = self.crear_objetos(filas)
        return filas
        

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
        self.insertar_id = False
        super().__init__()

class TablaVentas(TablaHija):
    def __init__(self) -> None:
        self.nombre_tabla = "Ventas"
        self.claseFila = Venta
        self.insertar_id = False
        super().__init__()
    
    def select_ultima_venta(self):
        filas = self.bd.consultar(f"SELECT * FROM ventas ORDER BY venta_id DESC LIMIT 1;")
        return self.crear_objetos(filas)

class TablaVentasIngresos(TablaHija):
    def __init__(self) -> None:
        self.nombre_tabla = "ventas_ingresos"
        self.claseFila = VentaIngreso
        self.insertar_id = False
        super().__init__()

class TablaVentasProductos(TablaHija):
    def __init__(self) -> None:
        self.nombre_tabla = "ventas_productos"
        self.claseFila = VentaProducto
        self.insertar_id = False
        super().__init__()
    
    def delete_por_producto(self,producto_id):
        return self.bd.ejecutar(f"DELETE FROM ventas_productos WHERE producto_id = {producto_id};")
class TablaTotalesDiarios(TablaHija):
    def __init__(self) -> None:
        self.nombre_tabla = "Totales_Diarios"
        self.claseFila = TotalDiario
        self.insertar_id = False
        super().__init__()

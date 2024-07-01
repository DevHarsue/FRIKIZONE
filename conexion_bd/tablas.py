from conexion_bd.objetos import *
from conexion_bd.tabla_hija import TablaHija

class TablaClientes(TablaHija):
    def __init__(self) -> None:
        self.nombre_tabla = "Clientes"
        self.claseFila = Cliente
        self.insertar_id = False
        super().__init__()
    
    def select_cedula(self,nacionalidad,cedula):
        filas = self.bd.consultar(f"SELECT * FROM {self.nombre_tabla} WHERE cliente_nacionalidad = '{nacionalidad}' AND cliente_cedula='{cedula}';")
        filas = self.crear_objetos(filas)
        return filas

    def calcular_clientes(self,año,mes):
        return self.bd.consultar(f"CALL calcular_cliente('{año}','{mes}');")
    
    def calcular_frecuencia_clientes(self,año,mes):
        return self.bd.consultar(f"CALL calcular_frecuencia_clientes('{año}','{mes}');")
        
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

    def calcular_mes(self,año,mes):
        return self.bd.consultar(f"CALL calcular_producto_mes('{año}','{mes}');")
        
class TablaUsuarios(TablaHija):
    def __init__(self) -> None:
        self.nombre_tabla = "Usuarios"
        self.claseFila = Usuario
        self.insertar_id = False
        super().__init__()
    
    def select_rol(self, rol: str) -> tuple:
        filas = self.bd.consultar(f"SELECT * FROM usuarios WHERE usuario_rol='{rol}'")
        filas = self.crear_objetos(filas)
        return filas

    def select_usuario(self,nombre):
        filas = self.bd.consultar(f"SELECT * FROM usuarios WHERE usuario_nombre='{nombre}'")
        filas = self.crear_objetos(filas)
        return filas

class TablaVentas(TablaHija):
    def __init__(self) -> None:
        self.nombre_tabla = "Ventas"
        self.claseFila = Venta
        self.insertar_id = False
        super().__init__()
    
    def select_ultima_venta(self):
        filas = self.bd.consultar(f"SELECT * FROM ventas ORDER BY venta_id DESC LIMIT 1;")
        return self.crear_objetos(filas)
    
    def select_fecha(self,fecha):
        filas = self.bd.consultar(f"SELECT * FROM ventas WHERE venta_fecha='{fecha}';")
        filas = self.crear_objetos(filas)
        return filas
    
    def select_cliente(self,id):
        filas = self.bd.consultar(f"SELECT * FROM ventas WHERE cliente_id='{id}';")
        filas = self.crear_objetos(filas)
        return filas

class TablaVentasIngresos(TablaHija):
    def __init__(self) -> None:
        self.nombre_tabla = "ventas_ingresos"
        self.claseFila = VentaIngreso
        self.insertar_id = False
        super().__init__()
    
    def select_venta(self,id):
        filas = self.bd.consultar(f"SELECT * FROM ventas_ingresos WHERE venta_id='{id}';")
        filas = self.crear_objetos(filas)
        return filas
    
    def delete_venta(self,id):
        return self.bd.ejecutar(f"DELETE FROM ventas_ingresos WHERE venta_id='{id}'")

class TablaVentasProductos(TablaHija):
    def __init__(self) -> None:
        self.nombre_tabla = "ventas_productos"
        self.claseFila = VentaProducto
        self.insertar_id = False
        super().__init__()
    
    def delete_por_producto(self,producto_id):
        return self.bd.ejecutar(f"DELETE FROM ventas_productos WHERE producto_id = {producto_id};")
    
    def delete_venta(self,id):
        return self.bd.ejecutar(f"DELETE FROM ventas_productos WHERE venta_id='{id}'")
    
class TablaTotalesDiarios(TablaHija):
    def __init__(self) -> None:
        self.nombre_tabla = "Totales_Diarios"
        self.claseFila = TotalDiario
        self.insertar_id = False
        super().__init__()
    
    def select_fecha(self, fecha) -> tuple:
        filas = self.bd.consultar(f"SELECT * FROM totales_diarios WHERE total_diario_fecha='{fecha}';")
        filas = self.crear_objetos(filas)
        return filas
    
    def select_mes(self,año,mes):
        filas = self.bd.consultar(f"SELECT * FROM totales_diarios WHERE total_diario_fecha>='{año}-{mes}-00' AND total_diario_fecha <= '{año}-{mes}-31';")
        filas = self.crear_objetos(filas)
        return filas
    
    def calcular_diario(self,fecha):
        return self.bd.consultar(f"CALL calcular_diario('{fecha}');")
    
    def calcular_mes_totales(self,año,mes):
        return self.bd.consultar(f"CALL calcular_mes_totales_diarios('{año}','{mes}');")
    
    def calcular_mes_ingresos(self,año,mes):
        return self.bd.consultar(f"CALL calcular_mes('{año}','{mes}');")

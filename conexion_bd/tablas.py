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
        

    def venta_diaria_producto(self,id: int,fecha: str) -> tuple:
        """
            Devuelve la cantidad que se vendio de un producto en un día
            
            Args:
                id (int): id del producto a examinar.
                fecha (str): fecha en formato 'YYYY-MM-DD'.
            
            Returns:
                Tuple: sigue la siguiente estructura (("NombreDivisa",numero_de_veces_vendido,total_en_divisa),...)
        """
        filas = self.bd.consultar(f"CALL calcular_ingreso_producto_diario({id},'{fecha}');")
        
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

class TablaTotalesDiarios(TablaHija):
    def __init__(self) -> None:
        self.nombre_tabla = "Totales_Diarios"
        self.claseFila = TotalDiario
        self.insertar_id = False
        super().__init__()
    
    def select_fecha(self,fecha: str) -> tuple:
        """
            Para seleccionar el total de ventas diarias por fecha
            
            Args:
                fecha (str): Fecha a buscar en formato 'YYYY-MM-DD'.
                
            Returns:
                Tuple: una tupla con los objetos TotalDiario
        """
        filas = self.bd.select(self.nombre_tabla,self._columnas,f"total_diario_fecha='{fecha}'")
        
        return self.crear_objetos(filas)
    
    def calcular_dia(self,fecha: str) -> None:
        """
            Para calcular cuanto se hizo en el dia e inserta directamente en la bd
            
            Args:
                fecha (str): Fecha a calcular en formato 'YYYY-MM-DD'.
            
            Returns:
                None.
        """
        filas = self.bd.consultar(f"CALL calcular_ingreso_diario('{fecha}');")
        for fila in filas:
            self.insert(fecha,fila[0],fila[2])

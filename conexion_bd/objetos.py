from abc import ABC

#Clase abstacta para cada objeto
class ObjetoPadre(ABC):
    pass

#Objetos para cada tabla

class Cliente(ObjetoPadre):
    def __init__(self,id: int,cedula: int,nacionalidad: str,nombre: str,apellido: str,direccion: str,telefono: str):
        self.id = id
        self.cedula = cedula
        self.nacionalidad = nacionalidad
        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion
        self.telefono = telefono
    
    def __repr__(self):
        return f'Cliente("{self.id}",{self.cedula},{self.nacionalidad},{self.nombre},{self.apellido},{self.direccion})'
    
    
class Usuario(ObjetoPadre):
    def __init__(self,id: int,nombre: str,contraseña: str,usuario_rol: str):
        self.id = id
        self.nombre = nombre
        self._contraseña = contraseña
        self.usuario_rol = usuario_rol
    
    def __repr__(self):
        return f'Usuario("{self.id}",{self.nombre},{self.usuario_rol})'

class Producto(ObjetoPadre):
    def __init__(self,id: int,nombre: str,descripcion: str,valor: float):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.valor = valor
    
    def __repr__(self):
        return f'Producto("{self.id}",{self.nombre},{self.descripcion},{self.valor})'   

class Venta(ObjetoPadre):
    def __init__(self,id: int,fecha: str,cliente_id: int):
        self.id = id
        self.fecha = fecha
        self.cliente_id = cliente_id
    
    def __repr__(self):
        return f'Venta("{self.id}",{self.fecha},{self.cliente_id})'

class VentaIngreso(ObjetoPadre):
    def __init__(self,id: int,venta_id: int,divisa_id: int,cantidad: float):
        self.id = id
        self.venta_id = venta_id
        self.divisa_id = divisa_id
        self.cantidad = cantidad
    
    def __repr__(self):
        return f'VentaIngreso("{self.id}",{self.venta_id},{self.divisa_id},{self.cantidad})'

class VentaProducto(ObjetoPadre):
    def __init__(self,id: int,venta_id: int,producto_id: int,cantidad: float):
        self.id = id
        self.venta_id = venta_id
        self.producto_id = producto_id
        self.cantidad = cantidad
    
    def __repr__(self):
        return f'VentaProducto("{self.id}",{self.venta_id},{self.producto_id},{self.cantidad})'
    
class Divisa(ObjetoPadre):
    def __init__(self,id: int,nombre: str,relacion: float):
        self.id = id
        self.nombre = nombre
        self.relacion = relacion
    
    def __repr__(self):
        return f'Divisa("{self.id}",{self.nombre},{self.relacion})'


class TotalDiario(ObjetoPadre):
    def __init__(self,id: int, fecha: str, divisa_id: int, total: float):
        self.id = id
        self.fecha = fecha
        self.divisa_id = divisa_id
        self.total = total
    
    def __repr__(self):
        return f'TotalDiario("{self.id}",{self.fecha},{self.divisa_id},{self.total})'
        

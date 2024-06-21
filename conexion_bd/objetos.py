from abc import ABC

#Clase abstacta para cada objeto
class ObjetoPadre(ABC):
    pass

#Objetos para cada tabla

class Cliente(ObjetoPadre):
    def __init__(self,id: int,nacionalidad: str,nombre: str,apellido: str,direccion: str,telefono: str):
        self.id = id
        self.nacionalidad = nacionalidad
        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion
        self.telefono = telefono
    
    def __repr__(self):
        return f'Cliente("{self.id}",{self.nombre},{self.apellido},{self.direccion})'
    
class Rol(ObjetoPadre):
    def __init__(self,id: int,nombre: str,permisos: str):
        self.id = id
        self.nombre = nombre
        self.permisos = permisos
    
    def __repr__(self):
        return f'Rol("{self.id}",{self.nombre},{self.permisos})'
    
class Usuario(ObjetoPadre):
    def __init__(self,id: int,nombre: str,apellido: str,direccion: str,contraseña: str,salt: str,rol_id: int):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion
        self.__contaseña = contraseña
        self.__salt = salt
        self.rol_id = rol_id
    
    def __repr__(self):
        return f'Usuario("{self.id}",{self.nombre},{self.apellido},{self.direccion},{self.rol_id})'

class Producto(ObjetoPadre):
    def __init__(self,id: int,nombre: str,descripcion: str,fecha: str,valor: float):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha = fecha
        self.valor = valor
    
    def __repr__(self):
        return f'Producto("{self.id}",{self.nombre},{self.descripcion},{self.fecha},{self.valor})'   

class Venta(ObjetoPadre):
    def __init__(self,id: int,fecha: str,cliente_id: int,usuario_id: int):
        self.id = id
        self.fecha = fecha
        self.cliente_id = cliente_id
        self.usuario_id = usuario_id
    
    def __repr__(self):
        return f'Venta("{self.id}",{self.fecha},{self.cliente_id},{self.usuario_id})'
    
class Divisa(ObjetoPadre):
    def __init__(self,id: int,nombre: str,relacion: float):
        self.id = id
        self.nombre = nombre
        self.relacion = relacion
    
    def __repr__(self):
        return f'Divisa("{self.id}",{self.nombre},{self.relacion})'

    
class Metodo(ObjetoPadre):
    def __init__(self,id: int,nombre: str,descipcion: str):
        self.id = id
        self.nombre = nombre
        self.descipcion = descipcion
    
    def __repr__(self):
        return f'Metodo("{self.id}",{self.nombre},{self.descipcion})'

class VentaDetalle(ObjetoPadre):
    def __init__(self,id: int,venta_id: int,producto_id: int,divisa_id: int,metodo_id: int,cantidad: int):
        self.id = id
        self.venta_id = venta_id
        self.producto_id = producto_id
        self.divisa_id = divisa_id
        self.metodo_id = metodo_id
        self.cantidad = cantidad
    
    def __repr__(self):
        return f'VentaDetalle("{self.id}",{self.venta_id},{self.producto_id},{self.divisa_id},{self.metodo_id},{self.cantidad})'
    
class TotalDiario(ObjetoPadre):
    def __init__(self,id: int, fecha: str, divisa_id: int, total: float):
        self.id = id
        self.fecha = fecha
        self.divisa_id = divisa_id
        self.total = total
    
    def __repr__(self):
        return f'TotalDiario("{self.id}",{self.fecha},{self.divisa_id},{self.total}'
        

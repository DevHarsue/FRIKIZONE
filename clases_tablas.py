from abc import ABC, abstractclassmethod
from conexion_base_datos import BaseDatos
from clases_objetos import *

class Tabla(ABC):
    @abstractclassmethod
    def __init__(self,bd: BaseDatos):
        self.bd = bd
        self.nombre_tabla = ""
        self.columnas = tuple()
        self.clase = None
    
    def select(self) -> None:
        """
            Obtiene los valores de la base de datos, para acceder a ellos usar .filas
            
            Args:
                None.
                
            Returns:
                None.
        """
        filas = self.bd.select(self.nombre_tabla,self.columnas)
        self.filas = list(map(lambda x: self.clase(*x),filas))
        self.filas = sorted(self.filas,key=lambda x: int(x.id))
    
    def insert(self,valores: tuple) -> None:
        """
            Inserta en la base de datos.
            
            Args:
                valores (tuple): Los valores a insertar en la base de datos.
                Para saber cuales columnas insertar puedes usar .columnas
            
            Returns:
                None
            
        """
        #Comprueba que se hayan cargado todos los valores
        if len(valores) != len(self.columnas) or isinstance(valores,str):
            raise FaltanValores(self.columnas)
        else:
            #se transforman los valores para crear el texto que se enviara a la bd
            valores_texto = ""
            for i,valor in enumerate(valores):
                valores_texto+="'"+str(valor)+"'"+ "," if i != len(valores)-1 else "'"+str(valor)+"'"
                
            bd.insert(self.nombre_tabla,self.columnas,valores_texto)
            self.filas.append(self.clase(*valores))
            self.filas = sorted(self.filas,key=lambda x: int(x.id))
            
    def update(self):
        pass
    
    def delete(self):
        pass


class TablaClientes(Tabla):
    def __init__(self,bd):
        super().__init__(bd)
        self.nombre_tabla = "clients"
        self.columnas = ("client_id","client_name","client_lastname","client_address")
        self.clase = Cliente


class FaltanValores(Exception):
    def __init__(self,columnas):
        super().__init__(f"Faltan valores o sobran, son {len(columnas)} columnas: {columnas}")


bd = BaseDatos()
tabla_clientes = TablaClientes(bd)
tabla_clientes.select()
# tabla_clientes.insert((5657218,"Miriam","Rivera","Calle 7"))
print(tabla_clientes.filas)
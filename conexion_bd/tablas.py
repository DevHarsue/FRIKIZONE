from conexion_bd.tabla_padre import TablaPadre
from conexion_bd.objetos import *

#Por ahora Es la unica tabla, esta deberia ser padre para cada tabla como tal
class TablaHija(TablaPadre):
    def __init__(self,nombre_tabla: str,claseFila,insertar_id: bool = True) -> None:
        super().__init__()
        self.nombre_tabla = nombre_tabla
        self.claseFila = claseFila
        self.definir_propiedades()
        self.insertar_id = insertar_id
    
    #Editamos el insert en caso que sean tablas que no requiera introducir el id
    def insert(self, *valores) -> tuple:
        print(valores)
        if (not self.insertar_id):
            id = self.columnas.pop(0)
            super().insert(*valores)
            self.columnas.insert(0,id)
        else:
            super().insert(valores)
    


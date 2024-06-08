from conexion_bd.tabla_padre import TablaPadre

class TablaHija(TablaPadre):
    def __init__(self) -> None:
        super().__init__()
        self.definir_propiedades()
    
    #Editamos el insert en caso que sean tablas que no requiera introducir el id
    def insert(self, *valores) -> None:
        if (not self.insertar_id):
            self._columnas.remove(self.columna_id)
            super().insert(*valores)
            self._columnas.insert(0,self.columna_id)
        else:
            super().insert(*valores)
    
    #Editamos el update en caso que sean tablas que no requiera introducir el id
    def update(self, id: int, valores: dict) -> None:
        if (not self.insertar_id):
            self._columnas.remove(self.columna_id)
            super().update(id,valores)
            self._columnas.insert(0,self.columna_id)
        else:
            super().update(id,valores)
    
    #Propiedad para acceder a las columnas que se deban insertar o updatear
    @property
    def columnas(self) -> list:
        if (not self.insertar_id):
            return self._columnas[1:]
        else:
            return self._columnas

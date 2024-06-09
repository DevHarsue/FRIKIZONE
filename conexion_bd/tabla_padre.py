from abc import ABC, abstractclassmethod
from conexion_bd.conexion_base_datos import BaseDatos

#Clase abstracta de tablas, contiene los metodos principales para cada tabla
class TablaPadre(ABC):
    @abstractclassmethod
    def __init__(self):
        self.bd = BaseDatos()
        self.nombre_tabla = ""
        #Este valor debe ser una clase hija de ObjetoPadre
        self.claseFila = None
        self.columna_id = ""
        self._columnas = list()
    
    #Para definir propiedades cuando se crea la tabla
    def definir_propiedades(self):
        descripcion_tabla = self.bd.consultar(f"DESCRIBE {self.nombre_tabla};")
        for descripcion in descripcion_tabla:
            self._columnas.append(descripcion[0])#Para agregar el nombre de la columna
        self.columna_id = self._columnas[0]
    
    def crear_objetos(self,filas,claseFila = None) -> tuple:
        """
            Funcion para crear objetos hijos de ObjetoPadre (revisar objetos.py)
            Args:
                filas: Este parametro es lo que devuelve la base de datos.
                claseFila: La clase a instanciar, sino se especifica se usa la de la tabla
            
            Returns:
                Tuple: devuelve una tupla con los objetos instanciados
        """
        if not claseFila:
            claseFila = self.claseFila
        return tuple(map(lambda x: claseFila(*x),filas))
    
    def select(self,id: int = -1) -> tuple:
        """
            Obtiene los valores de la tabla en una tupla
            Usar este metodo solo para pocos datos
            Args:
                id (int): buscar alguno por id especifico, sino se especifica trae todos
                
            Returns:
                Tuple: Datos que se seleccionaron (Es una tupla con objetos hijos de ObjetoPadre).
        """
        if id != -1:
            condicion = f"{self.columna_id}={id}"
        else:
            condicion = "TRUE"
            
        filas = self.bd.select(self.nombre_tabla,self._columnas,condicion)
        
        return self.crear_objetos(filas)
    
    def insert(self,*valores) -> None:
        """
            Inserta en la tabla.
            
            Args:
                *valores (*args): Los valores de las columnas a insertar en la tabla.
                Para saber cuales valores insertar puedes usar .columnas
            
            Returns:
                None
            
        """
        #Comprueba que se hayan cargado todos los valores
        if len(valores) != len(self._columnas) or isinstance(valores,str):
            raise FaltanValores(self._columnas)
        else:
            #se transforman los valores para crear el texto que se enviara a la bd
            valores_texto = ""
            for valor in valores:
                valores_texto+=f"'{valor}',"
            #Borra la coma del final
            valores_texto = valores_texto[:-1]
            
            self.bd.insert(self.nombre_tabla,self._columnas,valores_texto)
            
    def update(self,id: int,valores: dict) -> None:
        """
            Para actualizar la tabla.
            
            Args:
                id (int): id de la fila a actualizar.
                valores (dict): {"columna1":"valor1","columna2":"valor2",etc}
            Returns:
                None
        """
        
        #Comprobamos que la columnas que se van a actualizar existan
        for col in tuple(valores.keys()):
            encontrado = bool(tuple(filter(lambda c: c==col,self._columnas)))
            if not encontrado:
                raise NoExisteColumna(self._columnas)

        self.bd.update(self.nombre_tabla,(self.columna_id,id),valores)
    
    def delete(self,id: int) -> None:
        """
            Para borrar una fila de la tabla.
            
            Args:
                id (int): el id de la fila que desea borrar
            
            Returns:
                None
        """
        self.bd.delete(self.nombre_tabla,(self.columna_id,id))
    

#Exepciones que facilitaran el desarrollo
class FaltanValores(Exception):
    def __init__(self,columnas):
        super().__init__(f"Faltan valores o sobran, son {len(columnas)} columnas: {columnas}")

class NoExisteColumna(Exception):
    def __init__(self,columnas):
        super().__init__(f"La columna no existe, columnas disponibles: {columnas}")

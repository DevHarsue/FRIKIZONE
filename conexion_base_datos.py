import os
import mariadb

class BaseDatos:
    def __init__(self) -> None:
        #Diccionario de la configuracion para conectarse a la db, saca los datos de un archivo .env
        self.config = {
            "user": os.getenv("USER"),
            "password": os.getenv("PASSWORD"),
            "host": os.getenv("HOST"),
            "port": int(os.getenv("PORT")),
            "database": os.getenv("DATABASE")
        }
    
    # Metodo para ejecutar consultas sql que no devuelven datos
    def ejecutar(self,query: str) -> None:
        try:
            # Utilizo with, ya que de esta manera la conexion se cierra automaticamente
            with mariadb.connect(**self.config) as conn:
                cursor = conn.cursor()
                cursor.execute(query)
                conn.commit()
        except Exception as e:
            print(e)
            
    # Metodo que ejecuta el codigo sql y devuelve una lista con datos
    def consultar(self,query: str) -> list:
        try:
            # Utilizo with, ya que de esta manera la conexion se cierra automaticamente
            with mariadb.connect(**self.config) as conn:
                cursor = conn.cursor()
                cursor.execute(query)
                result = cursor.fetchall()
                return result
        except Exception as e:
            print(e)
    
    # Para seleccionar datos, se le pasa la tabla y las columnas
    def select(self,tabla: str,columnas: tuple) -> list:
        columnas_texto = ",".join(columnas)
        texto = f"SELECT {columnas_texto} FROM {tabla};"
        return self.consultar(texto)
    
    # Para insertar datos, se le pasa la tabla y las columnas con sus valores
    def insert(self,tabla: str,columnas: tuple,valores: tuple) -> None:
        columnas = ",".join(columnas)
        texto = f"INSERT INTO {tabla}({columnas}) VALUES({valores});"
        self.ejecutar(texto)
    
    # Para actualizar datos, se le pasa la tabla y los valores a actualizar en tuplas
    def update(self,tabla: str,valores: tuple) -> None:
        """
            Para actualizar datos en alguna tabla
            
            Args:
                tabla (str): nombre de la tabla.
                valores (tuple): los valores a actualizar > ((columna,"valor"),(columna2,"valor2"))
        """
        valores_texto = ""
        for columna,valor in valores:
            valores+= str(columna)+"="+"'"+str(valor)+"'"+","
        
        print(valores)
        # texto = f"INSERT INTO {tabla}({columnas}) VALUES({valores});"
        # self.ejecutar(texto)
    

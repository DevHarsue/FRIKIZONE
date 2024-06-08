import os
import mariadb
from dotenv import load_dotenv

class BaseDatos:
    def __init__(self) -> None:
        #Cargar las variables del .env
        load_dotenv()
        #Diccionario de la configuracion para conectarse a la db, saca los datos de un archivo .env
        #El archivo debe estar en este mismo directorio        
        self.configuracion = {
            "user": os.getenv("USER"),
            "password": os.getenv("PASSWORD"),
            "host": os.getenv("HOST"),
            "port": int(os.getenv("PORT")),
            "database": os.getenv("DATABASE")
        }
    
    #Metodo que retorna la conexion y el cursor
    def crear_conexion_cursor(self):
        conexion = mariadb.connect(**self.configuracion)
        cursor = conexion.cursor()
        return conexion,cursor
    
    # Metodo para ejecutar codigo sql que no devuelve datos
    def ejecutar(self,sql: str) -> None:
        try:
            conexion,cursor = self.crear_conexion_cursor()
            cursor.execute(sql)
        except Exception as e:
            conexion.rollback()
            print(e)
        
        conexion.commit()
        conexion.close()
        
    # Metodo para consultar datos a la base de datos
    def consultar(self,sql: str) -> tuple:
        try:
            conexion,cursor = self.crear_conexion_cursor()
            cursor.execute(sql)
            resultados = tuple(cursor.fetchall())
            return resultados
        except Exception as e:
            print(e)
            
        conexion.close()
        
    # Para seleccionar datos, se le pasa la tabla, columnas y la condicion
    def select(self,tabla: str,columnas: tuple,condicion: str) -> tuple:
        columnas_texto = ",".join(columnas)
        sql = f"SELECT {columnas_texto} FROM {tabla} WHERE {condicion};"
        return self.consultar(sql)
    
    # Para insertar datos, se le pasa la tabla y las columnas con sus valores
    def insert(self,tabla: str,columnas: tuple,valores: tuple) -> None:
        columnas = ",".join(columnas)
        sql = f"INSERT INTO {tabla}({columnas}) VALUES({valores});"
        self.ejecutar(sql)
    
    # Para actualizar datos, se le pasa la tabla, la columna_id con el id en una tupla
    # Y los valores a actualizar en un dict columna_nombre: valor 
    def update(self,tabla: str,id: tuple,valores: dict,) -> None:
        valores_texto = ""
        for k,v in zip(valores.keys(),valores.values()):
            valores_texto+= f"{k}='{v}',"
        
        #Borra la coma del final
        valores_texto = valores_texto[:-1]
        
        sql = f"UPDATE {tabla} SET {valores_texto} WHERE {id[0]}={id[1]};"
        self.ejecutar(sql)
    
    def delete(self, tabla: str, id: tuple) -> None:
        texto = f"DELETE FROM {tabla} WHERE {id[0]}={id[1]};"
        self.ejecutar(texto)
    

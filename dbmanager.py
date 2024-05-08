import mariadb
import os
from dotenv import load_dotenv

#Para cargar las variable de entorno (estan en un archivo .env)
load_dotenv()
class Data_Base:
    def __init__(self):
        #Diccionario de la configuracion para conectarse a la db, saca los datos de un archivo .env
        self.config = {
            "user": os.getenv("USER"),
            "password": os.getenv("PASSWORD"),
            "host": os.getenv("HOST"),
            "port": int(os.getenv("PORT")),
            "database": os.getenv("DATABASE")
        }
                
        #este diccionario servira para saber las columnas que tiene cada tabla 
        #Esto esta en fase de pruebas ya que podria haber una mejor manera de hacerlo
        self.dictionary_tables = {
            "products": "product_name,product_description,product_date,product_value",
            "employees": "employee_id,employee_name,employee_last_name,employee_address,employee_password,employee_salt,rol_id",
            "sales": "sale_date,client_id,employee_id",
            "sales_details": "sale_id,product_id,currency_id,method_id,sale_detail_quantity",
            "clients": "client_id,client_name,client_lastname,client_address",
            "methods": "method_name,method_description",
            "currencys": "currency_name,currency_relation",
            "rols" : "rol_name,rol_permissions"
        }
    
    # Metodo que ejecuta las consultas y devuelve ya sea datos, o un true o false
    # True o False devuelve si la operacion es un insert, update o delete, datos si es un select 
    def execute(self,query):
        
        # Utilizo with, ya que de esta manera la conexion se cierra automaticamente
        with mariadb.connect(**self.config) as conn:
            cursor = conn.cursor()
            cursor.execute(query)
            result = cursor.fetchall() if query.find("SELECT")!=-1 or query.find("DESCRIBE")!=-1 else True
            conn.commit()
            return result
        
    # Para seleccionar datos, se le pasan las tablas
    # si no se quieren todas las columnas se especifican los nombres uno por uno (no en iterable)
    def query_select(self,table,*args):
        columns = str(args).replace("(","").replace(")","").replace("'","") if len(args)>1 else args[0] if args else None
        
        # Comprueba si es un select de todo o de columnas especificos
        text = f"SELECT {columns} FROM {table}" if args else f"SELECT * FROM {table};"
        
        return self.execute(text)
    
    # Para insertar datos, se le pasa la tabla y los valores
    def query_insert(self,table,*args):
        # Busca en el diccionario cuales son las columnas que se deben insertar
        columns = self.dictionary_tables[f"{table}"]
        
        # Comprueba si el numero de elementos en args que se paso a la funcion es igual al numero de columns que pide la db
        # En caso que no dice cuales son
        if len(args) != len(columns.split(",")):
            return f"Las columnas son: {columns}"
        
        values = str(args).replace("(","").replace(")","")
        
        text = f"INSERT INTO {table}({columns}) VALUES({values});"
        
        return self.execute(text)
    
    # Para actualizar datos, se dice la tabla, el id(primary key) de la fila
    # los datos a actualizar se pasan como tuplas ("employee_name","hardware"),("employee_last_name","martinez")  
    def query_update(self,table,id,*args):
        # Comprobamos que los parametros que paso existen como columnas en la tabla
        columns = tuple(x[0] for x in self.execute(f"DESCRIBE {table};"))
        for update in args:
            error = list(filter(lambda x: x==update[0],columns))
            if not error:
                return f"Los parametros validos son: {columns}"
            
        # Creamos el texto que servira para la consulta 
        # debe quedar: employee_name="hardware",employee_last_name="martinez" 
        updates = ""
        for i,update in enumerate(args):
            updates += str(update[0]) +"="+ "'"+str(update[1])+"'" + ("," if i != len(args)-1 else "")
        
        # lo que esta despues del where es para quitar la "s" del nombre de la tabla y agregarle el "_id" 
        text = f"UPDATE {table} SET {updates} WHERE {table.replace(table,table[0:len(table)-1])+"_id"}={id};"
        
        return self.execute(text)
    
    # Para borrar se pasa la tabla y el id de la fila a borrar
    def query_delete(self,table,id):
        text = f"DELETE FROM {table} WHERE {table.replace(table,table[0:len(table)-1])+"_id"}={id};"
        
        return self.execute(text)
    

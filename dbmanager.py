import mariadb

class Data_Base:
    def __init__(self):
        self.conn = mariadb.connect(user = "user_system",password="0311",host="localhost",port=3306,database="frikizone")
        #este diccionario servira para saber los atributos que tiene cada tabla
        self.dictionary_tables = {
            "products": "product_name,product_description,product_date,product_value",
            "employees": "employee_id,employee_name,employee_last_name,employee_address,employee_password,employee_salt",
            "sales": "sale_date,client_id,employee_id",
            "sales_details": "sale_id,product_id,currency_id,method_id,sale_detail_quantity",
            "clients": "client_id,client_name,client_last_name,client_address",
            "methods": "method_name,method_description",
            "currencys": "currency_name,currency_relation",
            "rols" : "rol_name,rol_permissions"
        }
    
    # Metodo que ejecuta las consultas y devuelve ya sea datos, o un true o false
    # True o False devuelve si la operacion es un insert, update o delete, datos si es un select 
    def execute(self,query):
        try:
            cursor = self.conn.cursor()
            cursor.execute(query)
            result = cursor.fetchall() if query.find("SELECT")!=-1 else True
            self.conn.commit()
            return result
        except:
            return False
    
    # Tranforma algun iterable de la forma (2,"holas",232) a "2,'holas',232"
    def tranform_to_text(self,iterable):
        text = ""
        # En tal caso que el iterable no sea un interable
        if type(iterable) is int or type(iterable) is str:
            return iterable
        
        for i,element in enumerate(iterable):
            text += "'"+str(element)+"'"+"," if i!=len(iterable)-1 else "'"+str(element)+"'"
        return text
    
    # Para seleccionar datos, se le pasa la tabla
    # si no se quieren todos los datos se especifican los nombres uno por uno (no en iterable)
    def query_select(self,table,*args):
        atrs = self.tranform_to_text(args)
        
        # Comprueba si es un select de todo o de atributos especificos
        text = f"SELECT {atrs} FROM {table}" if len(args)>0 else f"SELECT * FROM {table};"
        
        return self.execute(text)
    
    # Para insertar datos, se le pasa la tabla y los valores
    def query_insert(self,table,*args):
        # Busca en el diccionario cuales son los atributos que se deben insertar
        atrs = self.dictionary_tables[f"{table}"]
        
        # Comprueba si el numero de parametros que se paso a la funcion es igual al numero de atrs que pide la db
        # En caso que no dice cuales son
        if len(args) != len(atrs.split(",")):
            return f"Los atributos son: {atrs}"
        
        values = self.tranform_to_text(args)
        
        text = f"INSERT INTO {table}({atrs}) VALUES({values});"
        
        return self.execute(text)
    
    # Para actualizar datos, se dice la tabla, el id(primary key) de la fila
    # los datos a actualizar se pasan como tuplas ("employee_name","hardware")("employee_last_name","martinez")  
    def query_update(self,table,id,*args):
        # Comprobamos que los parametros que paso existen como atrs en la tabla
        atrs = self.dictionary_tables[f"{table}"].split(",")
        for update in args:
            error = filter(lambda x: x==update[0],atrs)
            if not error:
                return False
            
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
    

db = Data_Base()
print(db.query_update("currencys",1,("currency_id",1)))
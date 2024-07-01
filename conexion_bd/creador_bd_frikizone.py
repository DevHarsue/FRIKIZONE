import subprocess
import mariadb
from dotenv import load_dotenv
import os

class Comprobador_BD():
    def __init__(self,configuracion) -> None:
        self.configuracion = configuracion
        try:
            with mariadb.connect(**self.configuracion) as conexion:
                cursor = conexion.cursor()
                cursor.execute("USE frikizone;")
        except Exception as e:
            if str(e) == "Unknown database 'frikizone'":
                self.crear_bd()
        

    def crear_bd(self):
        path = "conexion_bd/db.sql"
        command = ['mariadb', '-u', self.configuracion["user"] , f'-p{self.configuracion["password"]}']
        with open(path, 'rb') as sql_file:
            process = subprocess.Popen(command, stdin=sql_file, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = process.communicate()
        if str(stdout) != "b''" or str(stderr) != "b''":
            raise f"Error al crear la BD, stdout:{stdout},stderr:{stderr}"

class CrearEnv:
    def __init__(self) -> None:
        try:
            with open(".env", "r") as file:
                file.read()
                self.status = True
        except Exception as e:
            if str(e)!="[Errno 2] No such file or directory: '.env'":
                print(e)
            self.status = False
    
    def testear(self,usuario,contrasena,host,port):
        self.configuracion = {
            "user": usuario,
            "password": contrasena,
            "host": host,
            "port": port,
        }
        try:
            mariadb.connect(**self.configuracion)
            self.crear_env(usuario,contrasena,host,port)
            return True
        except Exception as e:
            print(e)
            return False
    
    def crear_env(self,usuario,contrasena,host,port):
        try:
            with open(".env", "w") as file:
                file.write(f"USER='{usuario}'\nPASSWORD='{contrasena}'\nHOST='{host}'\nPORT={port}\nDATABASE='frikizone'")
        except Exception as e:
            print(e)
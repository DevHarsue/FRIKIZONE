import subprocess
import mariadb

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


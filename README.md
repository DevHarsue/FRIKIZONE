# Importante.
Para ejecutar el codigo se necesita de un archivo que se llame ".env" que este dentro de la carpeta conexion_bd y que contenga la siguiente info:

USER = "usuario_de_mariadb"
PASSWORD = "contraseña_de_usuario_mariadb"
HOST = "localhost"
PORT = 3306
DATABASE = "frikizone" 

## Librerias necesarias:
1. python-dotenv
2. mariadb
3. pydolarVenezuela
4. requests
5. bs4
6. PyQt6
7. PySide6

## Programas necesarios:
1. MariaDB
2. QtDesigner


## Rutas en variable de entorno necesarias
1. C:\Program Files\MariaDB 11.3\bin

## Para transformar de .ui a .py
pyside6-uic ruta_del_ui -o ruta+nombre_nuevo_archivo.py
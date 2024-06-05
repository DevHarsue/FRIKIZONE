from conexion_bd.tablas import TablaHija
from conexion_bd.objetos import Producto
from conexion_bd.funciones_utiles import obtener_fecha

#Simple prueba de como funciona el codigo hasta ahora
#Esto obvio va a cambiar para no tener que introducirle la clase de los objetos que queramos que devuelvan
tabla_productos = TablaHija("productos",Producto,False)

# print(tabla_productos.columnas)
# tabla_productos.insert("Queso","Una Figura malandra",obtener_fecha(),100)
# tabla_productos.update(13,{"producto_nombre": "Figura Itadori"})
# tabla_productos.delete(13)
print(tabla_productos.select())
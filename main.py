from conexion_bd.tablas import TablaClientes,TablaDivisas,TablaMetodos,TablaProductos,TablaRoles,TablaUsuarios,TablaVentas,TablaVentasDetalles
from utilidades.funciones_utiles import obtener_fecha
from utilidades.scrapping_web_cne import BuscadorPersonas

buscador = BuscadorPersonas()
nombre = buscador.buscar_persona("V",31098480)
print(nombre)

# tabla = TablaVentasDetalles()
# print(tabla.columnas)
# tabla.insert(3,8,2,1,1)
# tabla.update(2,{"producto_id":4})
# tabla.delete(2)

# print(tabla.select())

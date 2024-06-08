from conexion_bd.tablas import TablaClientes,TablaDivisas,TablaMetodos,TablaProductos,TablaRoles,TablaUsuarios,TablaVentas,TablaVentasDetalles
from conexion_bd.funciones_utiles import obtener_fecha


tabla = TablaVentasDetalles()
# print(tabla.columnas)
# tabla.insert(3,8,2,1,1)
# tabla.update(2,{"venta_fecha":obtener_fecha()})
# tabla.delete(2)

print(tabla.select())

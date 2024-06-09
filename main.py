from conexion_bd.tablas import TablaClientes,TablaDivisas,TablaMetodos,TablaProductos,TablaRoles,TablaUsuarios,TablaVentas,TablaVentasDetalles,TablaTotalesDiarios
from utilidades.funciones_utiles import obtener_fecha,obtener_tasa_bcv
from utilidades.scrapping_web_cne import BuscadorPersonas

tabla = TablaTotalesDiarios()
print(tabla.columnas)
print(tabla.select_fecha("2024-06-08"))
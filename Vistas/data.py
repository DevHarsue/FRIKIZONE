from submain import MainWindow
from utilidades.funciones_utiles import obtener_fecha
from conexion_bd.tablas import TablaClientes,TablaProductos,TablaTotalesDiarios
from PySide6.QtCore import QDate
from PDF.clientes import ClientesPDF
from PDF.cierre_mensual import CierreMensualPDF
from PDF.productos import ProductosPDF
import os
import webbrowser

class VistaData:
    def __init__(self, ventana: MainWindow):
        self.ventana = ventana
        self.ui = ventana.ui
        self.ui.boton_cliente_data.pressed.connect(self.clientes)
        self.ui.boton_mensual_data.pressed.connect(self.mes)
        self.ui.boton_producto_data.pressed.connect(self.producto)
        self.informe_mes = False
        self.informe_cliente = False
        self.informe_producto = False
        fecha = obtener_fecha().split("-")
        self.ui.date_mensual.setDate(QDate(int(fecha[0]),int(fecha[1]),1))
        self.ui.boton_generar_informe.pressed.connect(self.generar)
        
    
    def cambiar_vista(self):
        self.ui.stacked_widget.setCurrentWidget(self.ui.vista_mensual)
    
    def clientes(self):
        self.cambiar_vista()
        self.informe_cliente = True
        self.informe_mes = False
        self.informe_producto = False
    
    def mes(self):
        self.cambiar_vista()
        self.informe_mes = True
        self.informe_cliente = False
        self.informe_producto = False
    
    def producto(self):
        self.cambiar_vista()
        self.informe_producto = True
        self.informe_mes = False
        self.informe_cliente = False
        
    def generar(self):
        fecha = self.ui.date_mensual.date().toString("yyyy-MM").split("-")
        if self.informe_cliente:
            clientes = TablaClientes().calcular_clientes(fecha[0],fecha[1])
            if not bool(clientes):
                self.ventana.mostrar_mensaje("Sin Informacion","No hay informacion para la fecha seleccionada")
                return 0
            
            clientes_ids = set()
            for x in clientes:
                clientes_ids.add(x[0])
            
            clientes_imprimir = []
            clientes_ids =tuple(clientes_ids)
            for c in clientes_ids:
                cliente_temp = tuple(filter(lambda x: x[0]==c,clientes))
                clientes_imprimir.append((c,cliente_temp[0][1],cliente_temp[0][2],cliente_temp[0][3],cliente_temp[0][-1],cliente_temp[1][-1],cliente_temp[2][-1]))
            clientes_frecuentes = TablaClientes().calcular_frecuencia_clientes(fecha[0],fecha[1])
            clientes_ordenados = []
            for x,veces in clientes_frecuentes:
                z = list(filter(lambda y: y[0]==x,clientes_imprimir))
                z = list(z[0])
                z.append(veces)
                clientes_ordenados.append(tuple(z))
            self.imprimir_clientes(clientes_ordenados)
        elif self.informe_mes:
            tabla = TablaTotalesDiarios()
            totales_ingresos = tabla.calcular_mes_ingresos(fecha[0],fecha[1])
            totales_cierres = tabla.calcular_mes_totales(fecha[0],fecha[1])
            if totales_cierres!=totales_ingresos:
                self.ventana.preguntar("Algunos dias no han sido cerrados","¿Desea generar total del mes aun sin cerrar algunos dias?")
                if not self.ventana.respuesta:
                    return 0
            if not bool(totales_cierres):
                self.ventana.mostrar_mensaje("Sin Informacion","No hay informacion para la fecha dada")
                return 0
            totales_diarios = tabla.select_mes(fecha[0],fecha[1])
            fechas = set()
            for x in totales_diarios:
                fechas.add(x.fecha)
            fechas = list(fechas)
            totales_imprimir = []
            for x in fechas:
                z = list(filter(lambda y: y.fecha==x,totales_diarios))
                totales_imprimir.append((x,z[0].total,z[1].total,z[2].total))
            
            self.imprimir_totales(totales_imprimir,totales_cierres)
        elif self.informe_producto:
            productos = TablaProductos().calcular_mes(fecha[0],fecha[1])
            self.imprimir_productos(productos)
                            
    def imprimir_clientes(self,clientes):
        fecha = self.ui.date_mensual.date().toString("yyyy-MM").split("-")
        pdf = ClientesPDF(fecha[0],fecha[1],clientes)
        documentos_path = str(os.path.expanduser("~\\Documents"))
        try:
            os.makedirs(documentos_path+"\\FRIKIZONE")
        except FileExistsError:
            pass
        path = f"{documentos_path}\\FRIKIZONE\\clientes_frecuentes_{fecha[0]}-{fecha[1]}.pdf"
        pdf.output(path)
        webbrowser.open_new(path)
        self.ui.stacked_widget.setCurrentWidget(self.ui.vista_data)
    
    def imprimir_totales(self,totales,cierre):
        fecha = self.ui.date_mensual.date().toString("yyyy-MM").split("-")
        pdf = CierreMensualPDF(fecha[0],fecha[1],totales,cierre)
        documentos_path = str(os.path.expanduser("~\\Documents"))
        try:
            os.makedirs(documentos_path+"\\FRIKIZONE")
        except FileExistsError:
            pass
        path = f"{documentos_path}\\FRIKIZONE\\cierre_mensual_{fecha[0]}-{fecha[1]}.pdf"
        pdf.output(path)
        webbrowser.open_new(path)
        self.ui.stacked_widget.setCurrentWidget(self.ui.vista_data)
        
    def imprimir_productos(self,imprimir):
        fecha = self.ui.date_mensual.date().toString("yyyy-MM").split("-")
        pdf = ProductosPDF(fecha[0],fecha[1],imprimir)
        documentos_path = str(os.path.expanduser("~\\Documents"))
        try:
            os.makedirs(documentos_path+"\\FRIKIZONE")
        except FileExistsError:
            pass
        path = f"{documentos_path}\\FRIKIZONE\\productos_{fecha[0]}-{fecha[1]}.pdf"
        pdf.output(path)
        webbrowser.open_new(path)
        self.ui.stacked_widget.setCurrentWidget(self.ui.vista_data)